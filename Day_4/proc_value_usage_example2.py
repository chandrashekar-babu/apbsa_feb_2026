from concurrent.futures import ProcessPoolExecutor as Executor
from multiprocessing import Process, Value, current_process as current

stats = {
    "usage_count": Value("i", 0),
    "connections": Value("i", 0)
}

from time import sleep

def handle_client():
    from random import random, randint
    from time import sleep

    print(f"handle_client invoked by {current().name}...")
    stats["connections"].value += 1

    while True:
        sleep(randint(1, 10))
        stats["usage_count"].value += 1 

def show_stats():
    from time import sleep
    while True:
        sleep(5)
        print(f"Usage: {stats['usage_count'].value}, Connections: {stats['connections'].value}")

if __name__ == '__main__':

    Process(target=show_stats).start()

    with Executor(max_workers=6) as workers:
        for i in range(6):
            workers.submit(handle_client)
  
  