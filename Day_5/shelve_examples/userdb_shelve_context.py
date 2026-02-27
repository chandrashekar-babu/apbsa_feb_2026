class UserDB(object):
    
    def __init__(self, filename):
        self.filename = filename
        self.opened = False

    def __check(self):
        if not self.opened: 
            raise ValueError, "must called within a context"

    def __enter__(self):
        import shelve
        self.__users = shelve.open(self.filename)
        self.opened = True
        return self

    def add(self, name, password, fullname):
        self.__check()
        if name in self.__users: 
            raise ValueError, "user '{0}' already exists.".format(name)
        
        self.__users[name] = {
            "username" : name,
            "password" : password,
            "fullname" : fullname
        }

    def modify(self, name, password=None, fullname=None):
        self.__check()
        if name not in self.__users: 
            raise ValueError, "user '{0}' does not exist.".format(name)
        
        self.__users[name] = {
            "username" : name,
            "password" : password if password else self.__users[name]["password"],
            "fullname" : fullname if fullname else self.__users[name]["fullname"]
        }
    
    def delete(self, name):
        self.__check()
        if name not in self.__users: 
            raise ValueError, "user '{0}' does not exist.".format(name)
        
        del self.__users[name] 


    def __exit__(self, *args):
        self.__users.close()
        self.opened = False


if __name__ == '__main__':
    
    with UserDB("testdb.dat") as users:
        users.add("john", "john123", "john doe")
        users.add("sam", "sam111", "Samuel Jones")
        users.add("adam", "adam123", "Adam Smith")




















