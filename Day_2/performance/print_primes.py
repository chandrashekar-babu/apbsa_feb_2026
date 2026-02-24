"""
A simple python program to test CPU performance by
generating a series of prime numbers
"""

from threading import Thread, current_thread
#from multiprocessing import Process as Thread, current_process as current_thread
from time import time
import sys

NUM_SERIES = 10_000_000
NUM_THREADS = 12 


def is_prime(number):
    """Returns True if 'number' is prime"""
    limit = int(number ** 0.5) + 1
    for d in range(2, limit):
        if number % d == 0:
            return False
    return True


def print_primes(start, stop):
    tname = current_thread().name

    while start < stop:
        if is_prime(start):
            print(f"{tname}: {start}")
        start += 1


if __name__ == '__main__':

    threads = []
    chunk_size = NUM_SERIES // NUM_THREADS

    start_time = time()
    for i in range(NUM_THREADS):
        start = i * chunk_size
        stop = (i * chunk_size) + chunk_size
        t = Thread(target=print_primes, args=(start, stop))
        t.start()
        threads.append(t)
        print(f"Created {t.name} with {start=}, {stop=}", file=sys.stderr)

    for t in threads:
        t.join()
    duration = time() - start_time

    print(f"{NUM_THREADS} Threads took {duration:.6f} seconds to complete",
          file=sys.stderr)
