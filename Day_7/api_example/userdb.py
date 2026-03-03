from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    password: str
    fullname: Optional[str]

class UserOpt(BaseModel):
    name: str
    password: Optional[str]
    fullname: Optional[str]

import sqlite3

class SQLiteConfig:
    dsn = {"database": "userdb.sqlite"}

    create_table = """
        CREATE TABLE users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(32) UNIQUE NOT NULL,
            password VARCHAR(32),
            fullname VARCHAR(32)
        )
    """

    insert_sql = """
        INSERT INTO users(name, password, fullname)
               VALUES(?,?,?)
    """

    delete_sql = """
        DELETE FROM users WHERE name = ?
    """

    select_all = """
        SELECT name, password, fullname FROM users
    """

    select_one = """
        SELECT name, password, fullname FROM users WHERE name = ?
    """

    replace_sql = """
        REPLACE INTO users(name, password, fullname) VALUES(?,?,?)
    """

    update_sql = """
        UPDATE users {fields} WHERE name = ?
    """

class MariaDBConfig:
    dsn = dict(host="192.168.1.5", username="pythonista", password="secret", database="training")
    create_table = """
        CREATE TABLE users(
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(32) UNIQUE NOT NULL,
            password VARCHAR(32),
            fullname VARCHAR(32)
        )
    """

    insert_sql = """
        INSERT INTO users(name, password, fullname)
               VALUES(?,?,?)
    """

    replace_sql = """
        INSERT OR REPLACE INTO users(name, password, fullname) VALUES(?,?,?)
    """

    delete_sql = """
        DELETE FROM users WHERE name = ?
    """

    update_sql = """
        UPDATE users {fields} WHERE name = ?
    """

    select_all = """
        SELECT name, password, fullname FROM users
    """

    select_one = """
        SELECT name, password, fullname FROM users WHERE name = ?
    """


class UserDB:
    def __init__(self, driver, config):
        self.config = config()
        self.driver = driver

    def connect(self):
        self.conn = self.driver.connect(**self.config.dsn)
        self.cursor = self.conn.cursor()

    def create_schema(self):
        self.cursor.execute(self.config.create_table)

    def add(self, user: User):
        self.cursor.execute(self.config.insert_sql,
                            (user.name, user.password, user.fullname))
        self.conn.commit()

    def get(self, username=None):
        if username is None:
            
            self.cursor.execute(self.config.select_all)
            for row in self.cursor:
                # field_names = "name", "password", "fullname"
                # fields = dict(zip(field_names, row))
                # yield User(**fields)
                yield User(name=row[0], password=row[1], fullname=row[2])
        else:
            self.cursor.execute(self.config.select_one, (username,))
            row = self.cursor.fetchone()
            yield User(name=row[0], password=row[1], fullname=row[2])


    def delete(self, username):
        self.cursor.execute(self.config.delete_sql, (username,))
        self.conn.commit()

    def replace(self, username, user):
        self.cursor.execute(self.config.replace_sql,
                            (username, user.password, user.fullname))
        self.conn.commit()

    def update(self, username, user):
        fields = []
        if user.password is not None:
            fields.append(f"SET password = '{user.password}'")
        
        if user.fullname is not None:
            fields.append(f"SET fullname = '{user.fullname}'")

        update_sql = self.config.update_sql.format(fields=",".join(fields))
        print(update_sql)
        self.cursor.execute(update_sql, (user.name,))
        self.conn.commit()


