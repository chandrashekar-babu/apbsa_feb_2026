from threading import Thread
from time import sleep
import itertools

def foo():
    for i in itertools.count():
        print("Running foo with i =", i)

def bar():
    for i in itertools.count():
        print("Running bar with i =", i)
             
if __name__ == "__main__":
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)    
    
    t1.start()
    t2.start()
    
    for i in range(5):
        print("Main thread is doing other work...")
        sleep(0.5)

    print("Main thread is waiting for foo and bar to finish...")
    t1.join()
    t2.join()
    print("All threads have finished.")