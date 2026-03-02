import sqlite3

select_sql = "SELECT * FROM emp"

db = sqlite3.connect("emp1.dat")

c = db.cursor()
c.execute(select_sql)

for row in c:
    print "id = %d, name = %s" % row

db.close()

