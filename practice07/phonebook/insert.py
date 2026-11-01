import psycopg2
from config import load_config


def insert_user(username, phone):

    sql = """INSERT INTO contacts(username, phone)
             VALUES(%s, %s) RETURNING id;"""

    user_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (username, phone,))

                rows = cur.fetchone()
                if rows:
                    user_id = rows[0]

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return user_id


def insert_many_users(user_list):

    sql = "INSERT INTO contacts(username, phone) VALUES(%s, %s)"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.executemany(sql, user_list)

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':

    name, phone = input("Name, phone: ").split()

    insert_user(name, phone)