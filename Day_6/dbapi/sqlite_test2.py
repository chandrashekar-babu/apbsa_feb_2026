#import sqlite3

#conn = sqlite3.connect("empdb.dat")

import oracle
conn = oracle.connect("oracle://hostname:port/schema/database", "user", "pass")
cursor = conn.cursor()

select_query = "SELECT * FROM emp"

cursor.execute(select_query)

for i, name, dept in cursor: print i, name, dept

conn.close()

