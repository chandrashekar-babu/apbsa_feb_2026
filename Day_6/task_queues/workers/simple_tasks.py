from celery import Celery

app = Celery('simple_tasks',
             backend='rpc://',
             broker='redis://localhost/')
# broker='pyamqp://guest@localhost//')



