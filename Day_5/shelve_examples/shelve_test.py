import shelve

from car import Car

c1 = Car("Honda")

data = shelve.open("data.dat")

data["name"] = "John"
data["visited"] = "delhi", "mumbai", "kolkatta"
data["car"] = c1

data.close()

