import sqlite3
import psycopg2


db_host = "192.168.1.8"
db_port = 5432
db_name = "postgres"
db_user = "postgres"
db_pass = "mysecretpassword"
db_table = "estabs_tbl"

def create_conn():
    conn = None
    try:
        conn = psycopg2.connect("dbname={} user={} host={} password={}".format(db_name,db_user,db_host,db_pass))
        cur = conn.cursor()
        cur.execute("select * from estabs_tbl")
        record = cur.fetchone()
        print(record)
        cur.close()
        conn.close()
        
    except:
        print("Cannot connect.")
    return conn

conn = psycopg2.connect("dbname={} user={} host={} password={}".format(db_name,db_user,db_host,db_pass))
cur = conn.cursor()
cur.execute(CREATE TABLE IF NOT EXISTS names_table (
    Id INTEGER PRIMARY,
    first_name text,
    last_name text,
    age integer
    );)
conn.commit()

cur.close()
conn.close()

conn = psycopg2.connect("dbname={} user={} host={} password={}".format(db_name,db_user,db_host,db_pass))
cur = conn.cursor()
cur.execute("INSERT INTO names_table VALUES(:Id, :first_name, :last_name, :age)",
              {'Id': None,
               'first_name': 'Gabriella',
               'last_name': 'Louise',
               'age': int(8)
              })
conn.commit()
cur.close()
conn.close()

conn = psycopg2.connect("dbname={} user={} host={} password={}".format(db_name,db_user,db_host,db_pass))
cur = conn.cursor()
cur.execute("SELECT first_name, last_name, age, MAX(rowid) FROM names_table")
record = cur.fetchone()
print(record)
cur.close()
conn.close()

conn = psycopg2.connect("dbname={} user={} host={} password={}".format(db_name,db_user,db_host,db_pass))
cur = conn.cursor()
cur.execute("INSERT INTO names_table VALUES(:Id, :first_name, :last_name, :age)",
              {'Id': None,
               'first_name': 'Maelle',
               'last_name': 'Levin',
               'age': int(5)
              })
conn.commit()
cur.close()
conn.close()

conn = psycopg2.connect("dbname={} user={} host={} password={}".format(db_name,db_user,db_host,db_pass))
cur = conn.cursor()
cur.execute("SELECT first_name, last_name, age, MAX(rowid) FROM names_table")
record = cur.fetchone()
print(record)
cur.close()
conn.close()