import sqlite3
conn = sqlite3.connect("mydata")

insert_sql = """
    INSERT INTO emp(name, dept) VALUES(?,?)
"""
cursor = conn.cursor()

while True:
    name = raw_input("Enter name: ")
    if not name: break
    dept = raw_input("Enter dept: ")
    cursor.execute(insert_sql, (name, dept))
    print "-" * 30

conn.commit()
conn.close()

