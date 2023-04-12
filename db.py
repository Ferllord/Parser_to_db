import os
import psycopg2
from dotenv import load_dotenv,find_dotenv

def _drop_db(conn):
    with conn.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS laptops;")
        print("Dropped")

def _create_db(conn):
    with conn.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS laptops("
                       "ID SERIAL PRIMARY KEY,"
                       "full_name VARCHAR(255) NOT NULL,"
                       "price VARCHAR(255) NOT NULL,"
                       "inches VARCHAR(255),"
                       "CPU VARCHAR(255),"
                       "SSD VARCHAR(255),"
                       "url VARCHAR(255) NOT NULL);")
        print("Created")


def _insert_db(conn,turple_of_lists):
    with conn.cursor() as cursor:
        for i in range(len(turple_of_lists[0])):
            full_name, price, inches, CPU, SSD, url = turple_of_lists
            full_names = full_name[i]
            prices = price[i]
            inchess = inches[i]
            CPUs = CPU[i]
            SSDs = SSD[i]
            urls = url[i]
            cursor.execute(f"INSERT INTO laptops(full_name,price,inches,CPU,SSD,url) VALUES('{full_names}','{prices}','{inchess}','{CPUs}','{SSDs}','{urls}');")


def _select_db(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM laptops LIMIT 5")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def _delete_db(conn):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM laptops WHERE full_name = 'vlad'")
        cursor.execute("ALTER SEQUENCE laptops_id_seq RESTART WITH 1")

def connection(turple_of_lists = ' '):
    load_dotenv(find_dotenv())
    host = os.getenv('HOST')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    db_name = os.getenv('DB_NAME')
    try:
        conn = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
        )
        conn.autocommit = True
        _drop_db(conn)
        _create_db(conn)
        _insert_db(conn,turple_of_lists)
        #_select_db(conn)
        # _delete_db(conn)
        print('Все прошло успешно')
    except Exception as e:
        print('Error: %s' % e)
        print('ConnectionError')
    finally:
        if conn:
            conn.close()
            print('Connection closed')