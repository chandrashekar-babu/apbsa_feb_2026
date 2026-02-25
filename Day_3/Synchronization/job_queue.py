from time import sleep

def square(x):
    sleep(5)
    return x*x

def factorial(x):
    sleep(3)
    from functools import reduce
    return reduce(lambda x,y: x*y, range(1, x+1))

def sum_all(x):
    sleep(2)
    return sum(range(x))


class MyJobQueue:

    def __init__(self, capacity):
        from queue import Queue
        from threading import Lock, Thread
        self.capacity = capacity
        self.jobq = Queue(capacity)
        self.workers = {}
        self.result = {}
        self.job_id = 0
        self.job_id_mtx = Lock()

        for i in range(capacity):
            self.workers[i] = Thread(target=self.work)
            self.workers[i].start()

    def work(self):
        while True:
            job_id, fn, args, kwargs = self.jobq.get()
            self.result[job_id] = fn(*args, **kwargs)
            self.jobq.task_done()

    def submit(self, fn, *args, **kwargs):
        with self.job_id_mtx: self.job_id += 1
        self.jobq.put((self.job_id, fn, args, kwargs))


    def join(self):
        self.jobq.join()
        return self.result

if __name__ == "__main__":

    jobs = MyJobQueue(10) # Upto 10 workers can run concurrently!

    jobs.submit(square, 10)
    jobs.submit(factorial, 5)
    jobs.submit(sum_all, 10)
    jobs.submit(square, 2)

    result = jobs.join() # Wait for all submitted jobs to complete...
    print("Result = {}".format(str(result)))

