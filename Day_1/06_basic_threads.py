from threading import Thread
from time import sleep
import itertools

def foo():
    for i in itertools.count():
        print(f"Foo: running as a thread: counting {i}")
        #sleep(1)

def bar():
    for i in itertools.count():
        print(f"Bar: running as a thread: counting {i}")
        #sleep(1)

if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)

    t1.start()
    t2.start()

    for i in itertools.count():
        print(f"Main: counting {i}")
        #sleep(1)

    t1.join()
    t2.join()
    print("Main: completed.")
