from redis import Redis
from rq import Queue
from simple_tasks import add

q = Queue(connection=Redis())
print(q.enqueue(add, 10, 20))

