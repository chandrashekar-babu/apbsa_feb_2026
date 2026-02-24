"""
A simple python program to test CPU performance by
generating a series of prime numbers
"""

from threading import Thread, current_thread
from time import time
import sys

import pyximport
pyximport.install()
from primes_cython import print_primes

NUM_SERIES = 1_000_000
NUM_THREADS = 4

if __name__ == '__main__':

    threads = []
    chunk_size = NUM_SERIES // NUM_THREADS

    for i in range(NUM_THREADS):
        start = i * chunk_size
        stop = (i * chunk_size) + chunk_size
        t = Thread(target=print_primes, args=(i+1, start, stop))
        print(f"Created {t.name} with {start=}, {stop=}", file=sys.stderr)
        threads.append(t)

    start = time()
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    duration = time() - start
    print(f"{NUM_THREADS} Threads took {duration} seconds to complete", 
            file=sys.stderr)
