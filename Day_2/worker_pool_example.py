#from concurrent.futures import ThreadPoolExecutor as Executor
#from threading import current_thread as current

from concurrent.futures import ProcessPoolExecutor as Executor
from multiprocessing import current_process as current

from time import sleep

def square(x):
    t_name = current().name
    print(f"square[{t_name}]: sleeping for 5 seconds...")
    sleep(5)
    print(f"square[{t_name}]: woke up...")
    return x*x

def cube(x):
    t_name = current().name
    print(f"cube[{t_name}]: sleeping for 5 seconds...")
    sleep(5)
    print(f"cube[{t_name}]: woke up...")
    return x*x*x

if __name__ == '__main__':
    with Executor(max_workers=5) as workers:
        r1 = workers.submit(square, 2)
        r2 = workers.submit(cube, 3)
        r3 = workers.submit(square, 5)
        r4 = workers.submit(cube, 7)
        print(f"Submitted work on workers...")
        print(r1, r2, r3, r4)

    print(f"All jobs complete")
    print(r1.result(), r2.result(), r3.result(), r4.result())
