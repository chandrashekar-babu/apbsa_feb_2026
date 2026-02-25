from threading import Thread
from queue import Queue

from time import sleep
from random import randint

queue = Queue(10)


def producer():
    while True:
        v = randint(1, 100)
        print("Produced: {}".format(v))
        queue.put(v, timeout=10)
        sleep(v/100.0)


def consumer():
    while True:
        v = queue.get(timeout=10)
        print("Consumed: {}".format(v))
        sleep((v/100.0) + 13)


p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()
