import sqlite3 as driver

connection_params = {
    "database": "/tmp/newdb"
}

CREATE_STAFF = """
CREATE TABLE IF NOT EXISTS staff
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32),
    role VARCHAR(32),
    dept VARCHAR(32)
)
"""

INSERT_STAFF = """
INSERT INTO staff (name, role, dept) VALUES(?,?,?)
"""

SELECT_ALL_STAFF = "SELECT * FROM staff"
