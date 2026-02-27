class Car:
    def __init__(self, name):
        import shelve
        self.__dict__['__store__'] = shelve.open(name + ".dat")
        #self.__dict__['__store__']['name'] = name
        self.name = name

    def __getattr__(self, attr):
        try:
            return self.__dict__['__store__'][attr]
        except KeyError:
            raise AttributeError, "%s instance has no attribute '%s'" % (
                                self.__class__.__name__, 
                                attr
                  )

    def __setattr__(self, attr, value):
        self.__dict__['__store__'][attr] = value
        self.__dict__['__store__'].sync()

    def info(self):
        print "{",
        for attr, value in self.__dict__['__store__'].items():
            print attr, ":", value, ",",
        print "}"

    def __del__(self):
        self.__dict__['__store__'].close()

    def drive(self):
        print "Driving car object"


