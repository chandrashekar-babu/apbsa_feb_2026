import shelve

class Car:
    store = shelve.open("Car.db")

    def __init__(self, name):
        if name not in Car.store:
            Car.store[name] = {'name': name}
        self.__dict__ = Car.store[name]

    def __del__(self):
        Car.store.sync()

    def drive(self):
        print "Driving car object"


