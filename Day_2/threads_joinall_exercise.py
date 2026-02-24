from time import sleep
from threading import Thread, current_thread
from random import randint

def joinall(threads, interval=None):
    pass # TODO: Implement the logic to wait for all threads to complete
         # It must allow reaping threads based on the order of exit.        

def joinall_simple(threads, interval=None):
    while threads:
        for t in threads:
            t.join(interval)
            if not t.is_alive():
                threads.remove(t)
                yield t

def joinall(threads, interval=None):
    from collections import deque
    threads = deque(threads)

    while threads:              # Example of a round-robin poll
        t = threads[0]
        t.join(interval)
        if not t.is_alive():
            yield threads.popleft()
        else:
            threads.rotate(-1)

def fn(count):
    th = current_thread()
    for i in range(count):
        print(f"In {th.name} counting {i}/{count}")
        sleep(0.5)

if __name__ == '__main__':
    threads = []
    for _ in range(5):
        t = Thread(target=fn, args=(randint(3, 25),))
        threads.append(t)
        t.start()

    # TODO: Implement this function.
    # First argument should be collection
    # of threads, second argument must
    # be tick interval

    for t in joinall(threads, 0.5):
        print(f"Thread {t.name} exited.")

    print("main complete")
