# pythran export is_prime(int)
def is_prime(number):
    limit = int(number ** 0.5) + 1
    for d in range(2, limit):
        if number % d == 0:
            return False
    return True


# pythran export print_primes(int, int, int)
def print_primes(tid, start, stop):

    while start < stop:
        if is_prime(start):
            print(f"Thread-{tid:d}: {start:d}")
        start += 1
