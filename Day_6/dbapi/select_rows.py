import sqlite3
conn = sqlite3.connect("mydata")

select_sql = """
   SELECT * FROM emp 
"""
cursor = conn.cursor()

cursor.execute(select_sql)

for row  in cursor:
    print "id: %d, name: %s, dept: %s" % row 

conn.close()

