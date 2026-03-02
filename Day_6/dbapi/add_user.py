from getpass import getpass
from hashlib import md5

def db_connect(dbtype):
    if dbtype == "sqlite3":
        import sqlite3
        return sqlite3.connect("accessdb")
    elif dbtype == "mysql":
        import MySQLDB
        return MySQLDB.connect(host="localhost", user="john")


conn = db_connect("sqlite3")


insert_sql = """
    INSERT INTO users(name, password) VALUES(?,?)
"""
cursor = conn.cursor()

while True:
    name = raw_input("Enter name: ")
    if not name: break
    password = md5(getpass("Enter password: ")).hexdigest()
    cursor.execute(insert_sql, (name, password))
    print "-" * 30

conn.commit()
conn.close()

