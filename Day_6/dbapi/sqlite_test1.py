import sqlite3

conn = sqlite3.connect("mydb")
cursor = conn.cursor()

create_table = """
               CREATE TABLE emp(
                        id   INT PRIMARY KEY, 
                        name VARCHAR(10), 
                        dept VARCHAR(10))
"""

cursor.execute(create_table)

insert_row = """
    INSERT INTO emp(id, name, dept) VALUES(%d, '%s', '%s')
"""

i = 1
while True:
    name = raw_input("Enter name: ")
    if not name: break
    dept = raw_input("Enter dept: ")
    cursor.execute(insert_row % (i, name, dept))
    i += 1

conn.commit()
conn.close()

