import mariadb as driver

DSN = {"host": "192.168.1.13", "user": "pythonista", "password": "secret", "database": "training"}

CREATE_USER_TABLE = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(32) UNIQUE NOT NULL,
        password VARCHAR(32),
        fullname VARCHAR(32)
    )
"""

INSERT_USER = """
    INSERT INTO users(name, password, fullname)
            VALUES(?,?,?)
"""

DELETE_USER = """
    DELETE FROM users WHERE name = ?
"""

SELECT_ALL_USER = """
    SELECT name, password, fullname FROM users
"""

SELECT_ONE_USER = """
    SELECT name, password, fullname FROM users WHERE name = ?
"""

REPLACE_USER = """
    REPLACE INTO users(name, password, fullname) VALUES(?,?,?)
"""

UPDATE_USER = """
    UPDATE users {fields} WHERE name = ?
"""
