import sqlite3
conn = sqlite3.connect("mydata")

create_sql = """
    CREATE TABLE emp(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32),
        dept VARCHAR(32)
    )
"""

conn.execute(create_sql)
conn.commit()
conn.close()

