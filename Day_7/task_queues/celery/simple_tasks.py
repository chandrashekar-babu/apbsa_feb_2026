from celery import Celery
from time import sleep

app = Celery(__name__,
             backend='rpc://',
             broker='redis://192.168.1.17/')
 #broker='pyamqp://rabbit@192.168.1.128//')

from time import sleep

count = 10_000_000

@app.task
def add(x, y):
    print("add called...")
    for i in range(count): pass

    return x + y

@app.task
def square(x):
    print(f"square invoked with x={x}...")
    sleep(10)
    return x*x
