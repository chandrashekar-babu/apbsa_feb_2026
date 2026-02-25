from queue import Queue
from threading import Thread

wait = Queue(1)

def foo():

    print("Waiting for bar..")
    wait.put(True)
    wait.join()
    print("Bar complete..")

def bar():
    from time import sleep
    sleep(3)
    wait.get()
    wait.task_done()

t1 = Thread(target=foo)
t2 = Thread(target=bar)
t1.start()
t2.start()



