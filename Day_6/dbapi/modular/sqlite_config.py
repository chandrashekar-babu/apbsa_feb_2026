import sqlite3 as driver
CREATE_TABLE_SQL = """CREATE TABLE users(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(32) UNIQUE,
                            role VARCHAR(32)
                   )"""

INSERT_SQL = """INSERT INTO users(name, role) VALUES(?, ?)"""

DSN = dict(database="users1.sqlite")

def connect():
    return driver.connect(**DSN)
    