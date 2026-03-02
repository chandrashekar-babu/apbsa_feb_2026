import sqlite3 as driver

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


class UserDB:
    def __init__(self, dsn):
        self.dsn = dsn
        self.conn = None

    def connect(self):
        self.conn = driver.connect(**self.dsn)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.close()

    def create_table(self):
        self.cursor.execute(CREATE_USER_SQL)

    def add(self, name, password, fullname):
        self.cursor.execute(INSERT_USER_SQL, (name, password, fullname))
    
    def modify(self, name, password=None, fullname=None):
        if password is None and fullname is None:  # TODO: Optimize this logic.
            raise ValueError("At least one of password or fullname must be provided.")
        elif password is not None and fullname is not None:
            query = " SET PASSWORD = ?, FULLNAME = ?"
            params = (password, fullname, name)
        elif password is not None:
            query = " SET PASSWORD = ?"
            params = (password, name)
        else:
            query = " SET FULLNAME = ?"
            params = (fullname, name)
 
        self.cursor.execute(UPDATE_USER_SQL + query + " WHERE NAME = ?", params)
        
    def delete(self, name):
        self.cursor.execute(DELETE_USER_SQL, (name,))

    def authenticate(self, name, password):
        self.cursor.execute(AUTH_USER_SQL, (name, password))
        return bool(self.cursor.fetchone()[0])
    
