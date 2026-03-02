from celery import Celery

app = Celery('multiply_task',
             backend='rpc://',
             broker='redis://localhost/')
# broker='pyamqp://guest@localhost//')

from time import sleep

count = 1000000000

@app.task
def mul(x, y):
    print("multiply called...")
    for i in range(count): pass

    return x * y


