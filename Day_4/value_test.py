#from threading import Thread as Task, current_thread as current
from multiprocessing import Process as Task, current_process as current, Value
from time import sleep

#class Value:
#    def __init__(self, ctype, value):
#        self.ctype = ctype
#        self.value = value

def foo(v):
    print(f'foo: {current().name} is running: Value = {v.value}')
    sleep(1)
    print(f'foo: {current().name}: Value now is {v.value}')
    v.value = 1000
    print(f'foo: {current().name}: Value now is {v.value}')

def bar(v):
    print(f'bar: {current().name} is running: Value = {v.value}')
    sleep(0.5)
    v.value += 100
    print(f'bar: {current().name}: Value now is {v.value}')
    sleep(0.5)
    print(f'bar: {current().name}: Value now is {v.value}')

if __name__ == '__main__':
    v = Value('i', 42)
    t1 = Task(target=foo, args=(v,))
    t2 = Task(target=bar, args=(v,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()