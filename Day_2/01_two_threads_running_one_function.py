# from gevent import monkey; monkey.patch_all()

from threading import Thread, current_thread as current
from time import sleep

def foo(count, delay):
    t = current()
    for i in range(count):
        print(f"In foo running as {t.name}: counting {i}")
        sleep(delay)

if __name__ == '__main__':
    t1 = Thread(target=foo, name="Counter", args=(5, 2))
    t2 = Thread(target=foo, name="Monitor", kwargs={"delay": 1, "count": 10})
    t1.start()
    t2.start()

    t1.join()
    t2.join()
