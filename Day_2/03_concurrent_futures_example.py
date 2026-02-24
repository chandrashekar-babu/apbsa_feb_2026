from gevent import monkey; monkey.patch_all()

from multiprocessing import current_process
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor as Executor
from time import sleep

def testfn():
    t = current_thread()
    p = current_process()
    for i in range(20):
        print(f"Process {p.name}, Thread {t.name}: counting {i}")
        sleep(1)
    
if __name__ == '__main__':
    with Executor(max_workers=6) as workers:
        r1 = workers.submit(testfn)
        r2 = workers.submit(testfn)
        r3 = workers.submit(testfn)
        print(f"Jobs submitted: future objects are: {r1}, {r2}, {r3}")
    
    print("-" * 30)
    #sleep(10)
    print("Tasks completed...")
