from multiprocessing import Pool

from time import sleep


def testfn():
    print("testfn invoked...")
    # sleep(2)
    exit(0)
    3 / 0

    print("testfn returns...")
    return 100


if __name__ == '__main__':
    pool = Pool(5)

    result = pool.apply_async(testfn)
    print("submitted a job...")
    # if result.ready():
    print(result.get())
