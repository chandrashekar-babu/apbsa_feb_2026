from multiprocessing import Process, Pipe
from producer_consumer import *

#from mypipe import Pipe

#class Pipe:
#    def __init__(self):
#        from Queue import Queue
#        self.queue = Queue(10)
#
#    def send(self, v):
#        self.queue.put(v)
#
#    def recv(self):
#        return self.queue.get()



send, recv = Pipe()

t1 = Process(target=producer, args=(send,))
t2 = Process(target=consumer, args=(recv,))

t1.start()
t2.start()

