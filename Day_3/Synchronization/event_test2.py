from threading import Thread, current_thread as current, Event
from time import sleep

nums = []
nums_initialized = Event()

def square():
    name = current().name
    print(f"{name}: waiting for numbers to be initialized, {nums=}")
    nums_initialized.wait()
    print(f"{name}: nums initialized - computing squares")
    result = [ n*n for n in nums ]
    print(f"{name}: {result=}")


def cube():
    name = current().name
    print(f"{name}: waiting for numbers to be initialized")
    nums_initialized.wait()
    print(f"{name}: nums initialized - computing squares")
    result = [n**3 for n in nums]
    print(f"{name}: {result=}")

def sum_nums():
    name = current().name
    print(f"{name}: waiting for numbers to be initialized")
    nums_initialized.wait()
    print(f"{name}: nums initialized - computing squares")
    result = sum(nums)
    print(f"{name}: {result=}")


if __name__ == '__main__':
    sqr = Thread(target=square, name="square-thread")
    c = Thread(target=cube, name="cube-thread")
    s = Thread(target=sum_nums, name="sum-thread")

    sqr.start()
    c.start()
    s.start()

    print(f"id(nums) = {id(nums)}")
    nums[:] = [int(v) for v in input("Enter numbers separated by space: ").split()]
    print(f"id(nums) = {id(nums)}")

    nums_initialized.set()
