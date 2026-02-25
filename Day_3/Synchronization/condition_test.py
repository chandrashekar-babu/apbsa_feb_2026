from threading import Thread, current_thread as current, Condition
from time import sleep

def testfn(c):
    name = current().name
    print(f"{name} waiting for a condition...")
    with c:
        c.wait()
    print(f"{name}: received condition notification.")

if __name__ == '__main__':
    c = Condition()
    threads = []
    for _ in range(5):
        t = Thread(target=testfn, args=(c,))
        t.start()
        threads.append(t)

    sleep(5)
    #for _ in range(5):
    #    with c:
    #        print("main-thread: sending notification...")
    #        c.notify()
    #    sleep(1)

    with c:
        print("main-thread: sending notification to all waiting threads")
        c.notify_all()
