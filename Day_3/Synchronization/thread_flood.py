from threading import Thread, current_thread
from time import sleep
from itertools import count

def foo():
    sleep(60)

if __name__ == '__main__':
    for i in count():
        t = Thread(target=foo)
        t.start()
        print("Created", t.name)
