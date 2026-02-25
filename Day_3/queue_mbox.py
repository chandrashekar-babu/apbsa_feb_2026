from threading import Thread
from queue import Queue
from random import sample, random
from time import sleep

SAMPLE_SIZE = 10

data_queue = Queue(SAMPLE_SIZE)
result_queue = Queue(SAMPLE_SIZE)


def producer(inbox, outbox):
    batch_count = 0
    while True:
        batch_count += 1
        dataset = sample(range(1, 100), 10)
        print("producer: batch {}, sample data = {}".format(
            batch_count, str(dataset)))
        for v in dataset:
            sleep(random())
            outbox.put(v)

        print("producer: waiting for batch {} to complete.".format(
            batch_count))
        outbox.join()

        result = []
        for v in range(SAMPLE_SIZE):
            result.append(inbox.get())
        print("producer: batch {} complete: result = {}.".format(
            batch_count, str(result)))
        inbox.task_done()


def consumer(n, inbox, outbox):
    while True:
        print("consumer-{}: waiting for value...".format(n))
        v = inbox.get()
        print("consumer-{}: got value: {}".format(n, v))
        sleep(random())
        if outbox.full():
            outbox.join()
        outbox.put(v*v)
        inbox.task_done()


p = Thread(target=producer, args=(result_queue, data_queue))
consumers = {}
for i in range(10):
    consumers[i+1] = Thread(target=consumer,
                            args=(i+1, data_queue, result_queue))
    consumers[i+1].start()

p.start()
