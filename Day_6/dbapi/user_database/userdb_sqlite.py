import sqlite3 as driver

CONNECTION = {"database": "users.sqlite"}

CREATE_TABLE_SQL = """
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) UNIQUE NOT NULL,
    password VARCHAR(32),
    dept VARCHAR(32),
    role VARCHAR(32)
)
"""

INSERT_SQL = """
INSERT INTO users(name, password, dept, role) VALUES(?,?,?,?)
"""

SELECT_ALL_SQL = """
SELECT name, dept, role from users
"""

SELECT_ONE_SQL = """
SELECT name, dept, role FROM users WHERE name = ?
"""

DELETE_SQL = """
DELETE FROM users WHERE name = ?
"""
