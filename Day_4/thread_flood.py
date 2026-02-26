from gevent import monkey; monkey.patch_all()  # Patch standard library for cooperative multitasking
from threading import Thread
import itertools
from time import sleep

for i in itertools.count(1):
    print(f"Thread {i} is starting.")
    Thread(target=sleep, args=(60,)).start()
