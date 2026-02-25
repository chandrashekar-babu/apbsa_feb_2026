from threading import Thread
from queue import Queue
from random import randint, random
from time import sleep

queue = Queue(1)

def foo():
    v = randint(1, 10)
    print("foo: generated value: {}".format(v))
    queue.put(v)
    print("foo: waiting for value to be consumed...")
    queue.join()
    print("foo: got consumer acknowledgement...")

    sleep(random())
    v = randint(1, 10)
    print("foo: generated value: {}".format(v))
    queue.put(v)
    print("foo: waiting for value to be consumed...")
    queue.join()
    print("foo: got consumer acknowledgement...")



def bar():
    sleep(random())
    v = queue.get()
    print("bar: got value: {}".format(v))
    queue.task_done()

    sleep(random())
    v = queue.get()
    print("bar: got value: {}".format(v))
    queue.task_done()


t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()
t2.start()




