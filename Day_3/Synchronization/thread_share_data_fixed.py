from __future__ import print_function

from threading import Thread, Lock

SIZE = 100000

a = list(range(SIZE))

lock = Lock()

def square_list_item(i):
        with lock:
            a[i] = a[i] * a[i]


def square_list_item_old(i):
    try:
        lock.acquire()
        a[i] = a[i] * a[i]
    finally:
        lock.release()

def square_list():
    for i in range(SIZE):
        square_list_item(i)

if __name__ == '__main__':
    t1 = Thread(target=square_list)
    t2 = Thread(target=square_list)

    #b = a.copy()
    b = list(a)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    for i, v in enumerate(a):
        if (b[i] ** 4) != v:
            print("a[{}] = {} NOT consistent with b[{}] ** 4 = {}".format(
                                                    i, v, i, b[i] ** 4))


