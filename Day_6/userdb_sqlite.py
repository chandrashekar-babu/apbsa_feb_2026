import sqlite3 as driver

dsn = {
    "database": "users.db"
}


CREATE_USER_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) UNIQUE NOT NULL,
    password VARCHAR(32) NOT NULL,
    fullname VARCHAR(32) NOT NULL
)
"""

INSERT_USER_SQL = """
INSERT INTO users (name, password, fullname) VALUES (?, ?, ?)
"""

UPDATE_USER_SQL = """
UPDATE users
"""

DELETE_USER_SQL = """
DELETE FROM users WHERE name = ?
"""

AUTH_USER_SQL = """
SELECT COUNT(*) FROM users WHERE name = ? AND password = ?
"""

