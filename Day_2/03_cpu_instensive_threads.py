from threading import Thread as Task, current_thread as current
from time import time
import os
NCPU = os.cpu_count()

def testfn():
    for i in range(1_000_000):
        pass


if __name__ == '__main__':
    tasks = []
    start = time()
    for i in range(NCPU):
        t = Task(target=testfn)
        t.start()
        tasks.append(t)

    for t in tasks:
        t.join()
    duration = time() - start
    print(f"All threads completed in {duration} seconds")
