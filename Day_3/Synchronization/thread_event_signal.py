from threading import Thread, current_thread, main_thread, Event
from time import sleep


def foo():
    th = current_thread()
    while not th.stop.is_set():
        print("foo invoked from:", th.name)
        sleep(2)
        main_thread().task_complete.set()
        print("foo sent a message....")


if __name__ == '__main__':
    foo_thread = Thread(target=foo)
    main_thread().task_complete = Event()
    foo_thread.stop = Event()
    foo_thread.start()

    print("main: waiting for foo to complete task...")
    main_thread().task_complete.wait()
    print("main: woke up by foo...")
    foo_thread.stop.set()
