from multiprocessing import Process, Queue, current_process


def producer(queue):
    for i in range(1000):
        queue.put("Sending message {}\n".format(i))


def consumer(queue):
    name = current_process().name
    while True:
        message = queue.get()
        print("consumer {} received: {}".format(name, message))


queue = Queue(100)

sender = Process(target=producer, args=(queue,))
sender.start()

workers = {}
for i in range(5):
    workers[i] = Process(target=consumer, args=(queue,))
    workers[i].start()
