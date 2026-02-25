from threading import Thread, Semaphore, Lock
from time import sleep
from random import randint
from collections import deque


class SimpleQueue:
    def __init__(self, size):
        self.queue = deque()
        self.reader = Semaphore(0)    # Null semaphore
        self.writer = Semaphore(size) # Counting semaphore
        self.lock = Lock()

    def __str__(self):
        with self.lock:
             s = f"SimpleQueue({list(self.queue)})"
        return s


    def put(self, v):

        self.writer.acquire()

        with self.lock: self.queue.append(v)

        self.reader.release()

    def get(self):
        self.reader.acquire()

        with self.lock: v = self.queue.popleft()

        self.writer.release()

        return v


queue = SimpleQueue(10)

def producer():
    while True:
        v = randint(1, 100)
        print("Produced: ", v, "Queue =", queue)
        queue.put(v)
        sleep(v/100.0)


def consumer():
    while True:
        v = queue.get()
        print("Consumed: ", v, "Queue =", queue)
        sleep((v/100.0) + 0.3)

p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()
