import sqlite3
conn = sqlite3.connect("accessdb")

create_sql = """
CREATE TABLE users(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    password VARCHAR(32) NOT NULL
)
"""

conn.execute(create_sql)
conn.commit()
conn.close()
