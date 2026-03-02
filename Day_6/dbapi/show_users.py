import sqlite3

conn = sqlite3.connect("accessdb")

select_sql = """
    SELECT * FROM users
"""

cursor = conn.execute(select_sql)

for uid, username, password in cursor:
    print "uid = {0}, name = {1}, password = {2}".format(uid, username, password)

conn.close()

    

