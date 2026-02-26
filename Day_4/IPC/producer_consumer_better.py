from multiprocessing import Process, Queue

from time import sleep
from random import randint

queue = Queue(10)

def producer(q):
    while True:
        v = randint(1, 100)
        print("Produced: ", v, "Queue =", q)
        q.put(v)
        sleep(v/100.0)


def consumer(q):
    while True:
        v = q.get()
        print("Consumed: ", v, "Queue =", q)
        sleep((v/100.0) + 0.3)

if __name__ == '__main__':
    p = Process(target=producer, args=(queue,))
    c = Process(target=consumer, args=(queue,))

    p.start()
    c.start()

