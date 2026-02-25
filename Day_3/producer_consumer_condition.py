from threading import Thread, Condition
from collections import deque

class SimpleQueue:
    def __init__(self, max_size=10):
        self.empty_slots = self.max_size = max_size
        self.queue = deque()
        self.queue_full = Condition()
        self.queue_empty = Condition()
        
    def __repr__(self):
        with self.queue_empty, self.queue_full:
            s = f"SimpleQueue({list(self.queue)})"
        return s
    
    def put(self, value):
        with self.queue_full:
            if self.empty_slots <= 0:
                self.queue_full.wait()

        with self.queue_empty:
            self.queue.append(value)
            self.empty_slots -= 1
            self.queue_empty.notify()

    def get(self):
        with self.queue_empty:
            if not self.queue:
                self.queue_empty.wait()

        with self.queue_full:
            v = self.queue.popleft()
            self.empty_slots += 1
            self.queue_full.notify()
        
        return v
    
if __name__ == '__main__':
    from random import randint, random
    from time import sleep

    queue = SimpleQueue(10)

    def producer():
        while True:
            v = randint(10, 99)
            queue.put(v)
            print(f"producer: adding {v}, {queue=}")
            sleep(random())

    def consumer():
        while True:
            sleep(random()*2)
            v = queue.get()
            print(f"consumer: fetched {v}, {queue=}")

    p = Thread(target=producer)
    c = Thread(target=consumer)
    p.start()
    c.start()