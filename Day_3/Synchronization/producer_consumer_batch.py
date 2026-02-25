from threading import Thread
from queue import Queue

from time import sleep
from random import randint
from collections import deque

BATCH_SIZE = 10

queue = Queue(BATCH_SIZE)

def producer():
    while True:
        for i in range(BATCH_SIZE):
            v = randint(1, 100)
            print("Produced: {}".format(v))
            queue.put(v)
        print("Submitted first batch....")
        queue.join()


def consumer():
    while True:
        for i in range(BATCH_SIZE-1):
            v = queue.get()
            print("Consumed: {}".format(v))
            sleep((v/100.0) + 0.3)
        queue.task_done()

p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()

