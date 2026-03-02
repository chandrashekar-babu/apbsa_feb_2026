class UserDB(object):
    
    def __init__(self, dbname):
        self.dbname = dbname
        self.opened = False

    def __check(self):
        if not self.opened: 
            raise ValueError, "must called within a context"

    def __enter__(self):
        import sqlite3
        self.db = sqlite3.connect(self.dbname) 
        self.opened = True
        return self
    
    def create_schema(self):
        query = """
            CREATE TABLE users(
                    name VARCHAR(32),
                    password VARCHAR(32),
                    fullname VARCHAR(32)
             )
        """
        self.db.execute(query)

    def exists(self, name):
        query = "SELECT COUNT(*) FROM users WHERE name = ?"
        cursor = self.db.cursor()
        cursor.execute(query, (name,))
        return bool(cursor.fetchone()[0])


    def add(self, name, password, fullname):
        self.__check()
        if self.exists(name): 
            raise ValueError, "user '{0}' already exists.".format(name)
      
        from hashlib import md5
        password = md5(password).hexdigest()
        query = "INSERT INTO users(name, password, fullname) VALUES(?,?,?)"
        self.db.cursor().execute(query, (name, password, fullname))

    def modify(self, name, password=None, fullname=None):
        self.__check()
        if not self.exists(name): 
            raise ValueError, "user '{0}' does not exist.".format(name)

        query = "UPDATE users SET "

        if password: 
            from hashlib import md5
            password = md5(password).hexdigest()
            query += "password = '{password}', ".format(password)

        if fullname: 
            query += "fullname = '{fullname}'".format(fullname)
        
        self.db.cursor().execute(query)
    
    def delete(self, name):
        self.__check()
        if not self.exists(name): 
            raise ValueError, "user '{0}' does not exist.".format(name)
        
        query = "DELETE FROM users WHERE name = ?"
        self.db.cursor().execute(query, (name,))

    def __exit__(self, *args):
        self.db.commit()
        self.db.close()
        self.opened = False

    def auth(self, name, password):
        pass # To be implemented

if __name__ == '__main__':
    
    with UserDB("userdatabase") as users:
        users.create_schema()
        users.add("john", "john123", "john doe")
        users.add("sam", "sam111", "Samuel Jones")
        users.add("adam", "adam123", "Adam Smith")


