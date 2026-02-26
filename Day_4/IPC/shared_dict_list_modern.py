from multiprocessing import Process, current_process
from multiprocessing.managers import SharedMemoryManager

from time import sleep

def foo(l):
    p = current_process()
    l[-1] = 100
    l[-2] = 56

def bar(l):
    p = current_process()
    sleep(0.5)
    print(f"In bar[{p.name}]: {list(l)=}")
    l[0] = 1234

if __name__ == '__main__':
    manager = SharedMemoryManager()
    manager.start()
    l = manager.ShareableList([22, 33, 44, 55])

    #l = [22, 33, 44, 55]

    proc1 = Process(target=foo, args=(l,))
    proc1.start()

    proc2 = Process(target=bar, args=(l,))
    proc2.start()

    proc1.join()
    proc2.join()
    print(f"In main: {list(l)=}")
