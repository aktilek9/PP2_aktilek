import psycopg2
from config import load_config


def query_by_username(username):

    sql = """SELECT * FROM contacts
             WHERE username = %s"""

    config = load_config()
    rows = []

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                cur.execute(sql, (username,))
                rows = cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    return rows

def query_by_phone(phone):

    sql = """ SELECT * FROM contacts
                WHERE phone LIKE %s"""

    config = load_config()
    rows = []

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                cur.execute(sql, (phone + "%",))
                rows = cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return rows

if __name__ == '__main__':
    contacts = query_by_phone("+")

    for contact in contacts:
        print(contact)