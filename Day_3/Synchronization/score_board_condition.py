from threading import Thread, Condition
from time import ctime, sleep
from random import random, randint
from sys import stdout

score = {
    "aaa" : 0,
    "bbb" : 0,
    "ccc" : 0
}

update = Condition()

def reader(name):
    while True:
        output = """
            ---------------------------------
            %s: %s: current score
            ---------------------------------
            %s
            *********************************
        """ 
        stdout.write(output % (ctime(), name, str(score)))
        stdout.flush()
        update.acquire()
        update.wait()
        update.release()

def writer():
    while True:
        sleep(random() * 10)
        score["aaa"] = randint(10, 100)
        score["bbb"] = randint(10, 100)
        score["ccc"] = randint(10, 100)

        update.acquire()
        update.notifyAll()
        update.release()

w = Thread(target=writer)

readers = { }

for i in range(5):
    readers[i] = Thread(target=reader, args=("Reader %d" % i, ))     
    readers[i].start()

w.start()







