import mariadb as driver

connection_params = {
    "host": "localhost",
    "username": "testuser",
    "password": "w3lc0me",
    "database": "newdb"
}

CREATE_STAFF = """
CREATE TABLE IF NOT EXISTS staff
(
    id   INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(32),
    role VARCHAR(32),
    dept VARCHAR(32)
)
"""

INSERT_STAFF = """
INSERT INTO staff (name, role, dept) VALUES(?,?,?)
"""

SELECT_ALL_STAFF = "SELECT * FROM staff"
