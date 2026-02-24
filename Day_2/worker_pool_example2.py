from gevent import monkey; monkey.patch_all()

from concurrent.futures import ThreadPoolExecutor as Executor
from threading import current_thread as current

#from concurrent.futures import ProcessPoolExecutor as Executor
#from multiprocessing import current_process as current, Queue

from time import sleep

data = [11, 2, 33, 44, 55, 66, 77]
result = Queue(len(data)*2)

def square(x):
    t_name = current().name
    print(f"square[{t_name}]: sleeping for 5 seconds...")
    sleep(5)
    print(f"square[{t_name}]: woke up...")
    result.put(("square", x*x))
    return x*x

def cube(x):
    t_name = current().name
    print(f"cube[{t_name}]: sleeping for 5 seconds...")
    sleep(5)
    print(f"cube[{t_name}]: woke up...")
    result.put(("cube", x*x*x))
    return x*x*x


if __name__ == '__main__':
    with Executor(max_workers=5) as workers:
        for d in data:
            print("Submitting", d)
            workers.submit(square, d)
            workers.submit(cube, d)

        print(f"Submitted work on workers...")
    
    for _ in range(len(data) * 2):
        print(result.get())
