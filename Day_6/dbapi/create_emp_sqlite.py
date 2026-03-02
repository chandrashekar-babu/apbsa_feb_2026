import sqlite3

create_sql = "CREATE TABLE emp(id INT PRIMARY KEY, name VARCHAR(32))"
insert_sql = "INSERT INTO emp(id, name) VALUES(?, ?)"

#db = sqlite3.connect(":memory:")

#db = MySQLdb.connect("hostname", "port", "username", "password", "database")
#db = MySQLdb.connect("mysql://hostname:port/database?username=joe&password=welcome")
db = sqlite3.connect("emp1.dat")
db.execute(create_sql)

c = db.cursor()
i = 1

values = []
while True:
    name = raw_input("Enter employee name: ")
    if name == "end": break
    values.append((i, name))
    i += 1

print "Values = ", values

c.executemany(insert_sql, values)

db.commit()
db.close()

