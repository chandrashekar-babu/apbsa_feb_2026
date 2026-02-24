from threading import Thread
from time import sleep
import threading

def testfn(n):
    if threading.current_thread() is threading.main_thread():
        print("testfn() is running in the main thread")
        for t in threading.enumerate():
            if t is not threading.current_thread():
                t.join()
                print(f"main_thread: {t.name} has finished")
    else:
        print("testfn() is running in a worker thread")
        for i in range(n):
            print(f"{threading.current_thread().name} is running iteration {i}")
            sleep(1)
        
if __name__ == "__main__":
    t1 = Thread(target=testfn, args=(7,), daemon=True)
    t1.start()

    t2 = Thread(target=testfn, args=(5,))
    t2.start()

    testfn(3)
    print("Main thread is exiting")
