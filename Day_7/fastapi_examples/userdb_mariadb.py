import mariadb as driver

dsn = {
    "database": "userdb",
    "user": "chandra",
    "host": "localhost",
}


CREATE_USER_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(32) UNIQUE NOT NULL,
    password VARCHAR(32) NOT NULL,
    fullname VARCHAR(32) NOT NULL
)
"""

INSERT_USER_SQL = """
INSERT INTO users (name, password, fullname) VALUES (?, ?, ?)
"""

UPDATE_USER_PASSWORD_AND_FULLNAME_SQL = """
UPDATE users
SET password = ?, fullname = ?
WHERE name = ?
"""

UPDATE_USER_PASSWORD_SQL = """
UPDATE users
SET password = ?
WHERE name = ?
"""

UPDATE_USER_FULLNAME_SQL = """
UPDATE users
SET fullname = ?
WHERE name = ?
"""

DELETE_USER_SQL = """
DELETE FROM users WHERE name = ?
"""

AUTH_USER_SQL = """
SELECT COUNT(*) FROM users WHERE name = ? AND password = ?
"""

