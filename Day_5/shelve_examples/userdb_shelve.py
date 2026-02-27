class UserDB(object):
    
    def __init__(self, filename):
        self.filename = filename
        import shelve
        self.__users = shelve.open(filename) 


    def add(self, name, password, fullname):
        if name in self.__users: 
            raise ValueError, "user '{0}' already exists.".format(name)
        
        self.__users[name] = {
            "username" : name,
            "password" : password,
            "fullname" : fullname
        }

    def modify(self, name, password=None, fullname=None):
        if name not in self.__users: 
            raise ValueError, "user '{0}' does not exist.".format(name)
        
        self.__users[name] = {
            "username" : name,
            "password" : password if password else self.__users[name]["password"],
            "fullname" : fullname if fullname else self.__users[name]["fullname"]
        }
    
    def delete(self, name):
        if name not in self.__users: 
            raise ValueError, "user '{0}' does not exist.".format(name)
        
        del self.__users[name] 


    def __del__(self):
        self.__users.close()


