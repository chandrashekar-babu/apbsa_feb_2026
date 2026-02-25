from threading import Thread, Event, Semaphore

from random import random, randint, sample
from time import sleep


data = []

updated = Event()


def update_data():
    while True:
        updated.clear()
        sleep(randint(1, 10))
        data[:] = sample(range(100), 10)
        updated.set()
        sleep(randint(1, 5))


def get_data(name):
    while True:
        print("{} waiting for list update...".format(name), flush=True)
        updated.wait()
        print("In {}: top 5 = {}\n".format(name, str(data[:5])), flush=True)
        print("In {}: bottom 5 = {}\n".format(
            name, str(data[-5:])), flush=True)


update_thread = Thread(target=update_data)

readers = {}

update_thread.start()

for i in range(5):
    readers[i] = Thread(target=get_data, args=("Reader-%d" % i,))
    readers[i].start()
