from concurrent.futures import ProcessPoolExecutor as Executor
from multiprocessing import current_process as current

from time import time, sleep

def square(x):
    sleep(0.5)
    return x*x

if __name__ == "__main__":
    data = [3, 2, 6, 8, 5, 9, 1, 4, 7]
    start = time()
    result = list(map(square, data))
    duration = time() - start
    print(f"map result: {result} duration={duration:.2f} seconds")

    start = time()
    with Executor(max_workers=12) as workers:
        result = list(workers.map(square, data))
    duration = time() - start
    print(f"parallel map result: {result} duration={duration:.2f} seconds")
