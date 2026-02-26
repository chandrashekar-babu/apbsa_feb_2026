#from threading import Thread
#from queue import Queue

from multiprocessing import Process, Queue

from time import sleep
from random import randint, random

queue = Queue(10)


def producer():
    while True:
        v = randint(1, 100)
        print("Produced: {}".format(v))
        queue.put(v)
        sleep(random())


def consumer():
    while True:
        v = queue.get()
        print("Consumed: {}".format(v))
        sleep(random())

if __name__ == '__main__':
    p = Process(target=producer)
    c = Process(target=consumer)

    p.start()
    c.start()
