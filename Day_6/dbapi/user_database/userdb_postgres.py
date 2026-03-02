import psycopg2 as driver

CONNECTION = {"host": "192.168.1.130", "user": "postgres", "password": "welcome", "database": "userdb"}

CREATE_TABLE_SQL = """
CREATE TABLE staff(
    id SERIAL,
    name VARCHAR(32) NOT NULL,
    password VARCHAR(32),
    dept VARCHAR(32),
    role VARCHAR(32)
)
"""

INSERT_SQL = """
INSERT INTO staff(name, password, dept, role) VALUES(%s, %s, %s, %s)
"""

SELECT_ALL_SQL = """
SELECT name, dept, role from staff
"""

SELECT_ONE_SQL = """
SELECT name, dept, role FROM staff WHERE name = %s
"""

DELETE_SQL = """
DELETE FROM staff WHERE name = %s
"""
