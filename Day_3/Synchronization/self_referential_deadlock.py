from threading import Lock

lock = Lock()

#lock.acquire()
#print "Acquired lock once..."

#lock.acquire()
#print "Acquired lock again..."

def bar():
    with lock:
        print("In bar function...")

def foo():
    with lock:
        print("In foo function...")
        bar()

foo()

