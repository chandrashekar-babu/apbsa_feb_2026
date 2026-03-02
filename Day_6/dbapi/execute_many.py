import sqlite3

data = [("bourne", "development"), ("adam", "admin"), ("jones", "marketing")]

conn = sqlite3.connect("mydata")

sql = "INSERT INTO emp(name, dept) VALUES(?,?)"

conn.executemany(sql, data)
conn.commit()
conn.close()


