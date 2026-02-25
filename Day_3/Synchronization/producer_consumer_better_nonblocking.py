from threading import Thread
#from Queue import Queue
from queue import Queue, Empty, Full

from time import sleep
from random import randint
from collections import deque

queue = Queue(10)

def producer():
    while True:
        v = randint(1, 100)
        print "Produced: ", v, "Queue =", queue
        try:
            queue.put(v, block=False)
        except Full:
            pass
        sleep(v/100.0)
        queue.join()


def consumer():
    while True:
        try:
            #v = queue.get(block=False)
            v = queue.get(timeout=10)
        except Empty:
           pass

        print "Consumed: ", v, "Queue =", queue
        sleep((v/100.0) + 0.3)
        queue.task_done()

p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()

