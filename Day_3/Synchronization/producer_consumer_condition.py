from threading import Thread, Condition, Lock
from time import sleep
from random import randint, random
from collections import deque


class SimpleQueue:
    def __init__(self, size=10):
        self.empty_slots = size
        self.queue = deque()
        self.empty = Condition()
        self.full = Condition()
        self.lock = Lock()

    def show(self):
        with self.lock:
            r = str(self.queue)
        return r

    def put(self, v):
        with self.full:
            if not self.empty_slots:
                self.full.wait()
       
        with self.empty:
            with self.lock:
                self.queue.append(v)
            self.empty_slots -= 1
            self.empty.notify()

    def get(self):
        with self.empty:
            if not self.queue:
                self.empty.wait()

       
        with self.full:
            with self.lock:
                v = self.queue.popleft()
            self.empty_slots += 1
            self.full.notify()

        return v


queue = SimpleQueue(10)


def producer():
    while True:
        v = randint(1, 100)
        print("Produced: ", v, "Queue =", queue.show())
        queue.put(v)
        sleep(random() / 10)


def consumer():
    while True:
        v = queue.get()
        print("Consumed: ", v, "Queue =", queue.show())
        sleep(random())


p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()
