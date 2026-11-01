import psycopg2
from config import load_config

def update_username(phone, new_username):

    updated_row_count = 0
    
    sql = """ UPDATE contacts
                SET username = %s
                WHERE phone = %s"""

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:


                cur.execute(sql, (new_username, phone))
                updated_row_count = cur.rowcount

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

def update_phone(username, new_phone):

    updated_row_count = 0

    sql = """ UPDATE contacts
                SET phone = %s
                WHERE username = %s"""

    config = load_config()
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
    
    
                cur.execute(sql, (new_phone, username))
                updated_row_count = cur.rowcount

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

if __name__ == '__main__':
    # update_username("+77714271895", "MARAL")

    update_phone("MARAL", "+77057056767")