#from concurrent.futures import ThreadPoolExecutor as Executor
#from threading import current_thread as current

from concurrent.futures import ProcessPoolExecutor as Executor
from multiprocessing import current_process as current

from time import sleep

def testfn(count):
    t = current()

    print(f"testfn[{t.name}] count={count} started")
    for i in range(5):
        print(f"testfn[{t.name}] count={count}: counting {i}")
        sleep(1)
    print(f"testfn[{t.name}] count={count}: done")


if __name__ == "__main__":
    with Executor(max_workers=3) as workers:
        for i in range(5):
            workers.submit(testfn, i)

    print("main: done")

