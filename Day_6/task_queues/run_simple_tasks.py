from simple_tasks import add, add_slow
from time import sleep

from rq import Queue
from redis import Redis

if __name__ == '__main__':
    r = add(3, 2)
    print(r)

    job_queue = Queue(name="simple_tasks_queue", connection=Redis("192.168.1.130"))
    job = job_queue.enqueue(add, 3, 2)
    
    while job.get_status() != "finished":
        if job.get_status() == "failed":
            print("Job failed. Re-queueing")
            job.requeue()
        else:    
            print("Polling for result: ", job.get_status())
            sleep(1)
    else:
        print(job.result)

    

