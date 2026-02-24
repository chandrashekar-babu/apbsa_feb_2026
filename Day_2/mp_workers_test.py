import multiprocessing as mp
#from concurrent.futures import ProcessPoolExecutor as Executor
from concurrent.futures import ThreadPoolExecutor as Executor
from time import sleep

def dummyfn():
    sleep(30)

with Executor(max_workers=mp.cpu_count()) as workers:
    workers.submit(dummyfn)


