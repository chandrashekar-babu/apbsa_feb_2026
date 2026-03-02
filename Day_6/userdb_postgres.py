import psycopg2 as driver

dsn = {
    "database": "userdb",
    "user": "chandra"
}


CREATE_USER_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) UNIQUE NOT NULL,
    password VARCHAR(32) NOT NULL,
    fullname VARCHAR(32) NOT NULL
)
"""

INSERT_USER_SQL = """
INSERT INTO users (name, password, fullname) VALUES (%s, %s, %s)
"""

UPDATE_USER_PASSWORD_AND_FULLNAME_SQL = """
UPDATE users
SET password = %s, fullname = %s
WHERE name = %s
"""

UPDATE_USER_PASSWORD_SQL = """
UPDATE users
SET password = %s
WHERE name = %s
"""

UPDATE_USER_FULLNAME_SQL = """
UPDATE users
SET fullname = %s
WHERE name = %s
"""

DELETE_USER_SQL = """
DELETE FROM users WHERE name = %s
"""

AUTH_USER_SQL = """
SELECT COUNT(*) FROM users WHERE name = %s AND password = %s
"""

