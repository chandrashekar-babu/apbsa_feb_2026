from concurrent.futures import ProcessPoolExecutor as Executor
from time import sleep


def testfn():
    print("testfn invoked...")
    # sleep(2)
    exit(0)
    3 / 0
    
    print("testfn returns...")
    return 100


if __name__ == '__main__':
    with Executor(max_workers=5) as pool:
        result = pool.submit(testfn)
        print("submitted a job...")
        # if result.ready():
        print(result.result())
