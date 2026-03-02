import sqlite3

insert_sql = """
    INSERT INTO users(name, password) VALUES (?, ?)
"""

create_sql = """
    CREATE TABLE users(
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    name        VARCHAR(32),
                    password    VARCHAR(32)
    )
"""

select_sql = """
    SELECT COUNT(*) FROM users WHERE name = ? AND password = ?
"""

class Users:
    
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)

    def create(self):
        self.conn.execute(create_sql)
        self.conn.commit()

    def add(self, username, password):
        from hashlib import md5
        self.conn.execute(insert_sql, (username, md5(password).hexdigest()))
        self.conn.commit()

    def auth(self, username, password):
        from hashlib import md5
        cursor = self.conn.execute(select_sql, (username, md5(password).hexdigest()))
        c, =  cursor.next()
        return bool(c)

    def __del__(self):
        self.conn.commit()
        self.conn.close()



