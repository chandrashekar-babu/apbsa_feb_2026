from threading import Thread
from time import sleep
import threading

def testfn(n):
    for i in range(n):
        active_threads = [ t.name for t in threading.enumerate() if t.is_alive() ]
        print(f"Thread is running: {i}, active threads: {active_threads}")
        sleep(1)

if __name__ == "__main__":
    t1 = Thread(target=testfn, args=(150,), daemon=True)
    t1.start()

    t2 = Thread(target=testfn, args=(3,))
    t2.start()

    testfn(5)
    # t1.join() # NEVER join a daemon thread, it will never finish.
    print("Main thread is exiting")
