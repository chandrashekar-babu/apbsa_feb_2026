from random import randint
from threading import Thread, current_thread, Barrier
from time import sleep

msg_barrier = Barrier(10)

def random_sleep_and_print():
    thread_name = current_thread().name
    v = randint(5, 30)
    sleep(v)
    print(f"{thread_name}: Woke up!")
    msg_barrier.wait()
    print(f"{thread_name}: Continuing!")


if __name__ == '__main__':
    threads = {}
    for i in range(10):
        threads[i] = Thread(target=random_sleep_and_print)
        threads[i].start()
