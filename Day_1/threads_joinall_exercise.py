from time import sleep
from threading import Thread, current_thread
from random import randint

def joinall_old(threads, interval=None):
    while threads:
        for t in threads:
            t.join(timeout=interval)
            if not t.is_alive():
                threads.remove(t)
                yield t
        
def joinall(threads, interval=0.5):
    from collections import deque
    threads = deque(threads)
    while threads:
        t = threads[0]
        t.join(timeout=interval)
        if not t.is_alive():
            yield threads.popleft()
        else:
            threads.rotate(-1)
        

def fn(count):
    th = current_thread()
    for i in range(count):
        print(f"In {th.name} counting {i}/{count}")
        sleep(0.5)
    print(f"{th.name} completed...")

if __name__ == '__main__':
    threads = []
    for _ in range(5):
        t = Thread(target=fn, args=(randint(3, 25),))
        threads.append(t)
        t.start()

    # TODO: Implement the following function.
    # First argument should be collection
    # of threads, second argument must
    # be tick interval

    for t in joinall(threads, 0.5):
        print(f"Thread {t.name} exited.")

    #for t in threads:
    #    t.join()
    #    print(f"Thread {t.name} exited.")


    print("main complete")
