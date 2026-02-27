import shelve
from car import Car
from person import Person

store = shelve.open("data.dat")

name = "James"

info = {'city' : 'Chennai', 'temperature' : 38, 'country' : 'India' }

scores = [555, 66, 23, 432, 77, 22]

p = Person("James")
c = Car("Honda")

store['n'] = name
store['info'] = info
store['marks'] = scores

store['p'] = p
store['car'] = c


store.close()


