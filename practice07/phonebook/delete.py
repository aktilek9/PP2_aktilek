import psycopg2
from config import load_config


def delete_by_username(username):

    sql = """DELETE FROM contacts
             WHERE username = %s"""

    config = load_config()
    deleted_rows = 0

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (username,))
                deleted_rows = cur.rowcount

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    if deleted_rows == 0:
        print("User not found")
    else:
        print("User deleted successfully")


def delete_by_phone(phone):

    sql = """DELETE FROM contacts
             WHERE phone = %s"""

    config = load_config()
    deleted_rows = 0

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (phone,))
                deleted_rows = cur.rowcount

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    if deleted_rows == 0:
        print("User not found")
    else:
        print("User deleted successfully")


if __name__ == '__main__':
    delete_by_username("Jordan")