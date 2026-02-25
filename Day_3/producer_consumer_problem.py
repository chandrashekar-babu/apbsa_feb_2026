from threading import Thread
from random import randint, random
from time import sleep
from collections import deque

data = deque()

def producer():
    while True:
        v = randint(10, 99)
        data.append(v)
        print(f"producer: adding {v}, {data=}")
        sleep(random())


def consumer():
    while True:
        sleep(random() / 2)
        v = data.popleft()
        print(f"consumer: fetched {v}, {data=}")


if __name__ == '__main__':
    p = Thread(target=producer)
    c = Thread(target=consumer)
    p.start()
    c.start()
