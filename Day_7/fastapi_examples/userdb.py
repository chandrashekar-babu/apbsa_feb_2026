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


class UserDB:
    def __init__(self, config):
        self.config = config
        self.driver = config.driver

    def connect(self):
        self.conn = self.driver.connect(**self.config.DSN)
        self.cursor = self.conn.cursor()

    def create_schema(self):
        self.cursor.execute(self.config.CREATE_USER_TABLE)

    def add(self, user: User):
        self.cursor.execute(self.config.INSERT_USER,
                            (user.name, user.password, user.fullname))
        self.conn.commit()

    def get(self, username=None):
        if username is None:
            
            self.cursor.execute(self.config.SELECT_ALL_USER)
            for row in self.cursor:
                # field_names = "name", "password", "fullname"
                # fields = dict(zip(field_names, row))
                # yield User(**fields)
                yield User(name=row[0], password=row[1], fullname=row[2])
        else:
            self.cursor.execute(self.config.SELECT_ONE_USER, (username,))
            row = self.cursor.fetchone()
            yield User(name=row[0], password=row[1], fullname=row[2])


    def delete(self, username):
        self.cursor.execute(self.config.DELETE_USER, (username,))
        self.conn.commit()

    def replace(self, user: User):
        self.cursor.execute(self.config.REPLACE_USER,
                            (user.name, user.password, user.fullname))
        self.conn.commit()

    def update(self, user: UserOpt):
        fields = []
        if user.password is not None:
            fields.append(f"SET password = '{user.password}'")
        
        if user.fullname is not None:
            fields.append(f"SET fullname = '{user.fullname}'")

        update_sql = self.config.UPDATE_USER.format(fields=",".join(fields))
        print(update_sql)
        self.cursor.execute(update_sql, (user.name,))
        self.conn.commit()