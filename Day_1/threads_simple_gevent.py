from gevent import monkey
monkey.patch_all()

from threading import Thread
from time import sleep

def foo(n):
    while n > 0:
        print("Running foo with n =", n)
        n -= 1
        sleep(0.5)

def bar(n):
    while n > 0:
        print("Running bar with n =", n)
        n -= 1
        sleep(0.5)

if __name__ == "__main__":
    t1 = Thread(target=foo, args=(10,))
    t2 = Thread(target=bar, args=(10,))
    
    t1.start()
    t2.start()
    
    for i in range(5):
        print("Main thread is doing other work...")
        sleep(0.5)

    print("Main thread is waiting for foo and bar to finish...")
    t1.join()
    t2.join()
    print("All threads have finished.")