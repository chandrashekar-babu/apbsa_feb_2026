from celery import Celery
from celery.schedules import crontab

from time import sleep

app = Celery(__name__,
             backend='rpc://',
             broker='redis://192.168.1.13/')
 #broker='pyamqp://rabbit@192.168.1.128//')


#app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
#    'add-every-monday-morning': {
#        'task': 'testfn',
#        'schedule': crontab(minute=1),
#    },
#}

from time import sleep

count = 500_000_000

@app.task
def add_busy(x, y):
    print(f"add_busy({x}, {y}) invoked...")
    for i in range(count): pass
    print(f"add_busy({x}, {y}) returning {x+y}")
    return x + y

@app.task
def add_slow(x, y):
    print(f"add_slow({x}, {y}) invoked...")
    sleep(10)
    print(f"add_slow({x}, {y}) returning {x+y}")
    return x + y


@app.task
def testfn():
    print("testfn invoked...")
    sleep(10)
    return 100
