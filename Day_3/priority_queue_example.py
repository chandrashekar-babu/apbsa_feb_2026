from threading import Thread
from queue import PriorityQueue

from time import sleep
from random import randint
from collections import deque

queue = PriorityQueue(10)

for i in range(10):
    value = input("Enter a value: ")
    #queue.put((len(value), value))
    queue.put(value)

for i in range(10):
    v = queue.get()
    print("Value:", v)


