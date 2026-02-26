from multiprocessing import Process, current_process
from multiprocessing import Manager

from time import sleep

def foo(d, l):
    p = current_process()
    print(f"In foo[{p.name}]: {dict(d)=}, {list(l)=}")
    d["name"] = "Smith"
    d["role"] = "Admin"
    l.append(100)
    l.append(56)

def bar(d, l):
    p = current_process()
    sleep(0.5)
    print(f"In bar[{p.name}]: {dict(d)=}, {list(l)=}")
    d["name"] = d["name"].upper()
    l[0] *= 10

if __name__ == '__main__':
    manager = Manager()
    d = manager.dict()
    l = manager.list()

    proc1 = Process(target=foo, args=(d, l))
    proc1.start()

    proc2 = Process(target=bar, args=(d, l))
    proc2.start()

    proc1.join()
    proc2.join()
    print(f"In main: {dict(d)=}, {list(l)=}")
