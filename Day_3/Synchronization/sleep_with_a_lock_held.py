from __future__ import print_function
from threading import Thread, Lock, current_thread
import itertools
from time import sleep
from sys import getswitchinterval

sleep_lock = Lock() # Non-reentrant lock

def sleeping_function():
    t = current_thread()
    for i in itertools.count():
        with sleep_lock:
            print(f"In {t.name}: sleeping with count = {i}")
            sleep(1)
            print(f"In {t.name}: woke up with count = {i}")
        sleep(getswitchinterval())

if __name__ == '__main__':

    t1 = Thread(target=sleeping_function)
    t2 = Thread(target=sleeping_function)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
