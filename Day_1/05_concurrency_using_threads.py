# from gevent import monkey; monkey.patch_all()

from threading import Thread
from time import sleep

def foo():
    for i in range(10):
        print(f"In foo: counting {i}")
        sleep(1)

def bar():
    for i in range(10):
        print(f"In bar: counting {i}")
        sleep(1)

if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)
    t1.start()
    t2.start()

    t1.join()
    t2.join()
