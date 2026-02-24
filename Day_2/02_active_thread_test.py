from threading import Thread, current_thread as current
from time import sleep

def foo(count, delay):
    t = current()
    for i in range(count):
        print(f"{t.name}: counting {i}")
        sleep(delay)

if __name__ == '__main__':
    t1 = Thread(target=foo, args=(5, 1))
    t2 = Thread(target=foo, kwargs={"delay": 1, "count": 10})
    t3 = Thread(target=foo, args=(15, 2), daemon=True)
    
    t1.start()
    t2.start()

    #t3.daemon = True
    t3.start()

    foo(7, 1)
    print("Main exited...")