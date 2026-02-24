"""
A simple python program to test CPU performance by
generating a series of prime numbers
"""

# from threading import current_thread as current
# from concurrent.futures import ThreadPoolExecutor as Executor
from multiprocessing import current_process as current
from concurrent.futures import ProcessPoolExecutor as Executor
from time import time
import sys

NUM_SERIES = 1_000_000
NUM_THREADS = 4


def is_prime(number):
    """Returns True if 'number' is prime"""
    limit = int(number ** 0.5) + 1
    for d in range(2, limit):
        if number % d == 0:
            return False
    return True


def print_primes(start, stop):
    """Store prime numbers from start to stop into primes
    list passed as arguments
    """
    tname = current().name

    while start < stop:
        if is_prime(start):
            print(f"{tname}: {start}")
        start += 1


if __name__ == '__main__':

    chunk_size = NUM_SERIES // NUM_THREADS
    futures = []

    start_time = time()
    with Executor(max_workers=NUM_THREADS) as executor:
        for i in range(NUM_THREADS):
            start = i * chunk_size
            stop = (i * chunk_size) + chunk_size
            r = executor.submit(print_primes, start, stop)
            print(f"Created Thread-{i+1} with {start=}, {stop=}",
                  file=sys.stderr)
            futures.append(r)

        for r in futures:
            r.result()

    duration = time() - start_time

    print(f"{NUM_THREADS} Threads took {duration:.6f} seconds to complete",
          file=sys.stderr)
