from multiprocessing import Process, Pipe, current_process


def producer(out):
    for i in range(1000):
        out.send("Sending message {}\n".format(i))


def consumer(inp):
    name = current_process().name
    while True:
        message = inp.recv()
        print("consumer {} received: {}".format(name, message))


send, recv = Pipe()

sender = Process(target=producer, args=(send,))
sender.start()

workers = {}
for i in range(5):
    workers[i] = Process(target=consumer, args=(recv,))
    workers[i].start()
