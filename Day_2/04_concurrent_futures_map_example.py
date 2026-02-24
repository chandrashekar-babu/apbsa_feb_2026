from gevent import monkey; monkey.patch_all()

from threading import current_thread as current
from concurrent.futures import ThreadPoolExecutor as Executor

#from multiprocessing import current_process as current
#from concurrent.futures import ProcessPoolExecutor as Executor

from time import sleep, ctime, time

def square(v):
    t = current()
    print(f"square({v}): invoked by {t.name}")
    sleep(1)
    #for _ in range(100_000_000): pass
    return v*v

nums = [3, 5, 2, 8, 6, 7, 13, 12, 17, 16, 18]
nums *= 1000

#result = []
#for v in nums:
#    r = square(v)
#    result.append(r)

if __name__ == '__main__':
    with Executor(max_workers=6000) as p:
        print("Start time: ", ctime())
        start = time()
        #result = list(map(square, nums))
        #result = [ square(v) for v in nums ]

        result = list(p.map(square, nums))

    duration = time() - start

    print(f"End time: {ctime()}, {result=}, {duration=}")
