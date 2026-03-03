from userdb_mariadb import *

class UserDB:
    def __init__(self):
        self.driver = driver
        self.dsn = dsn  
        self.conn = None

    def connect(self):
        self.conn = self.driver.connect(**self.dsn)
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
        #if password is None and fullname is None:  # TODO: Optimize this logic.
        #    raise ValueError("At least one of password or fullname must be provided.")
        #elif password is not None and fullname is not None:
        #    query = " SET PASSWORD = ?, FULLNAME = ?"
        #    params = (password, fullname, name)
        #elif password is not None:
        #    query = " SET PASSWORD = ?"
        #    params = (password, name)
        #else:
        #    query = " SET FULLNAME = ?"
        #    params = (fullname, name)
 
        if password is None and fullname is None:
            raise ValueError("At least one of password or fullname must be provided.")
        elif password is not None and fullname is not None:
            query = UPDATE_USER_PASSWORD_AND_FULLNAME_SQL
            params = (password, fullname, name)
        elif password is not None:
            query = UPDATE_USER_PASSWORD_SQL
            params = (password, name)
        else:
            query = UPDATE_USER_FULLNAME_SQL
            params = (fullname, name)

        self.cursor.execute(query, params)
        
    def delete(self, name):
        self.cursor.execute(DELETE_USER_SQL, (name,))

    def authenticate(self, name, password):
        self.cursor.execute(AUTH_USER_SQL, (name, password))
        return bool(self.cursor.fetchone()[0])
    
