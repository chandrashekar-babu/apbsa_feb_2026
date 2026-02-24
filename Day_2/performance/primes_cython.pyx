#cython: language_level = 3

import cython

@cython.locals(limit=cython.uint, d=cython.uint, number=cython.uint)
def is_prime(unsigned int number):
    "Returns True if 'number' is prime"
    limit = int(number ** 0.5) + 1
    for d in range(2, limit):
        if number % d == 0:
            return False
    return True

def print_primes(tid: cython.uint, start: cython.uint, stop: cython.uint):
    while start < stop:
        if is_prime(start):
            print(f"Thread-{tid}: {start}")
        start += 1
