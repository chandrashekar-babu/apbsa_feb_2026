from multiprocessing import Pool, current_process as current, cpu_count
from time import sleep, ctime, time

def square(v):
    t = current()
    print(f"square({v}): invoked by {t.name}")
    sleep(1)
    return v*v

nums = [3, 5, 2, 8, 6, 7, 13, 12, 17, 16, 18]

#result = []
#for v in nums:
#    r = square(v)
#    result.append(r)

if __name__ == '__main__':
    p = Pool(cpu_count())

    print("Start time: ", ctime())
    start = time()
    #result = list(map(square, nums))
    #result = [ square(v) for v in nums ]

    result = list(p.map(square, nums))

    duration = time() - start

    print(f"{result=}, {duration=}")
