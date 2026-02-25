from threading import Thread, Condition, Lock
from random import randint, random
from time import sleep
from collections import deque

class SynchronizedQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = deque()
        self.full = Condition()
        self.empty = Condition()
        self.qlock = Lock()


    def __str__(self):
        with self.qlock:
            s = str(self.queue)
        return s

    def put(self, value):
        with self.full:
            if len(self.queue) >= self.capacity:
                self.full.wait()

        with self.empty, self.qlock:
            self.queue.append(value)
            self.empty.notify()

    def get(self):
        with self.empty:
            if not self.queue:
                self.empty.wait()

        with self.full, self.qlock:
            v = self.queue.popleft()
            self.full.notify()

        return v

data = SynchronizedQueue(10)

def producer():
    while True:
        v = randint(10, 99)
        print("producer: adding {}, queue = {}".format(v, data))
        data.put(v)
        sleep(random()  / 2)

def consumer():
    while True:
        v = data.get()
        print("consumer: fetched {}, queue = {}".format(v, data))
        sleep(random())

if __name__ == '__main__':
    #for i in range(4):
    #    Thread(target=producer).start()
    p = Thread(target=producer)
    p.start()

    #for i in range(4):
    #    Thread(target=consumer).start()

    c = Thread(target=consumer)
    c.start()
