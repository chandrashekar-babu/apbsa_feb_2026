#!/usr/bin/env python
from threading import Thread
import time
from Queue import Queue

class Send(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.count = 0
 
    def run(self):
        while True:
            self.count += 1
            self.queue.put(self.count)
            time.sleep(1)

class Recieve(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            print "Count: ", self.queue.get()
            time.sleep(1)

def test():
    data_queue = Queue(10)

    sender = Send(data_queue)
    reciever = Recieve(data_queue)

    sender.start()
    reciever.start()


 
