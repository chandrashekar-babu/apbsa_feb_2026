# Needs Python 3 
from queue import Queue

from threading import Thread
from time import sleep
from random import randint, random


mutex = Queue(1)

def fn(name):
    while True:
        key = randint(1, 100)
        print("{}: entering critical section: key={}".format(name,key))
        mutex.put(key)
        print("{}: in critical section: key={}".format(name, key))
        sleep(random())
        print("{}: exiting critical section: key={}".format(name, key))
        exit_key = mutex.get()
        print("{}: out of critical section: key={}, exit_key={}".format(name, key,
                                                                         exit_key))

foo = Thread(target=fn, args=("foo",))
bar = Thread(target=fn, args=("bar",))

foo.start()
bar.start()




