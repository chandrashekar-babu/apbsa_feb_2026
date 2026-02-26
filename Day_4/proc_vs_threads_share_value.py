#from threading import Thread as Task, current_thread as current
from multiprocessing import Process as Task, current_process as current

from multiprocessing import Value
#class Value:
#    def __init__(self, ctype, value):
#        self.value = value

from time import sleep

def foo(n):
    t = current()
    print(f"In foo[{t.name}]: v = {n.value}")
    sleep(1)
    n.value = 500
    print(f"In foo[{t.name}]: v now is {n.value}")

def bar(n):
    t = current()
    print(f"In bar[{t.name}]: v ={n.value}")
    sleep(2)
    print(f"In bar[{t.name}]: v now is {n.value}")


if __name__ == '__main__':
    num = Value("i", 54356)

    t1 = Task(target=foo, args=(num,))
    t2 = Task(target=bar, args=(num,))

    print(f"{t1=}, {t2=}")

    t1.start()
    t2.start()
