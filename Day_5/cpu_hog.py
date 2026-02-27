import time
import math
import os

def expensive_calculation():
    """A function that eats CPU cycles."""
    result = 0
    for i in range(10**7):
        result += math.sqrt(i)
    return result

def fast_function():
    """A function that finishes quickly."""
    time.sleep(0.1)

def main():
    print(f"CPU-hog started. Pid = {os.getpid()}")
    while True:
        expensive_calculation()
        fast_function()

if __name__ == "__main__":
    main()