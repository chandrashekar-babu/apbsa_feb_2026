from __future__ import print_function
from threading import Thread

SIZE = 1000000

nums = list(range(SIZE))
        
def square_list_item(i):
        v = nums[i]
        nums[i] = v*v

def square_list():
    for i in range(SIZE):
        square_list_item(i)

if __name__ == '__main__':
    t1 = Thread(target=square_list)
    t2 = Thread(target=square_list)

    #backup = nums.copy()
    backup = list(nums)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    for i, v in enumerate(nums):
        if (backup[i] ** 4) != v:
            print(
                "nums[{}] = {} NOT consistent with backup[{}] ** 4 ={}".format(i, v, i, backup[i] ** 4))
