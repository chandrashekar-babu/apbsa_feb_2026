from threading import Thread, current_thread
import threading

from time import sleep

def counter(c):
    th = current_thread()
    name = th.name
    for i in range(c):
        if hasattr(th, "cancel"):
            break
        print(f"{name}: counting {i}")
        sleep(10)

if __name__ == '__main__':
    intervals = (10, 7, 15, 20)

    for i in intervals:
        Thread(target=counter, args=(i,)).start()

    sleep(2)
    print("Exiting main: waiting for threads to terminate....")
    for t in threading.enumerate():
        t.cancel = True

    for t in threading.enumerate():
        if t is not threading.main_thread():
            t.join()
            print(f"{t.name} exited.")


