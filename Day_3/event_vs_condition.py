from threading import Thread, Condition, Event
from time import sleep

c = Condition()
e = Event()

def foo():
    print("In foo: waiting for condition 1...")
    with c: c.wait()

    print("In foo: waiting for condition 2...")
    with c: c.wait()

    print("In foo: waiting for condition 3...")
    with c: c.wait()

def bar():
    print("In bar: waiting for condition 1...")
    e.wait()

    print("In bar: waiting for condition 2...")
    e.wait()

    e.clear()
    print("In bar: waiting for condition 3...")
    e.wait()
    print("In bar: got event 3...")


th = Thread(target=bar)
th.start()

print("Main: started foo...")

sleep(1)
print("Main: sending notification for condition 1...")
e.set()

sleep(2)
print("Main: setting event again...")
e.set()

#with c: c.notify_all()

#sleep(2)
#print("Main: sending notification for condition 2...")
#with c: c.notify()

#sleep(3)
#print("Main: sending notification for condition 3...")
#with c: c.notify()






