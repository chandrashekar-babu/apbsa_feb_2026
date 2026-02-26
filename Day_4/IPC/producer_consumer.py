from time import sleep
from random import random, randint
from multiprocessing import Process, Pipe

def producer(pipe):
    while True:
        val = randint(10, 1000)
        print("producer: produced data %d\n" % val)
        pipe.send(val)
        sleep(random())


def consumer(pipe):
    while True:
        val = pipe.recv()
        print("consumer: received %d\n" % val)
        sleep(random())

if __name__ == '__main__':
    write_end, read_end = Pipe()

    p = Process(target=producer, args=(write_end,))
    c = Process(target=consumer, args=(read_end,))
    p.start()
    c.start()

