#from threading import Thread as Task

from multiprocessing import Process as Task

data = []

def foo():
    data.append(100)

def bar():
    from time import sleep
    sleep(1)
    print("In bar: data = ", data)

if __name__ == '__main__':
    t1 = Task(target=foo)
    t2 = Task(target=bar)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
