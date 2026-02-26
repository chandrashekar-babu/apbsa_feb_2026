from multiprocessing import Process, current_process
from multiprocessing.shared_memory import SharedMemory
from time import sleep

def foo(s):
    p = current_process()
    print(f"In foo[{p.name}]: {s.buf[0]=}")
    s.buf[0] = 11
    sleep(1)
    print(f"In foo[{p.name}]: {s.buf[0]=}")

def bar(s):
    p = current_process()
    print(f"In bar[{p.name}]: {s.buf[0]=}")
    sleep(0.5)
    print(f"In bar[{p.name}]: {s.buf[0]=}")
    s.buf[0] = 33

if __name__ == '__main__':
    shm = SharedMemory(create=True, size=10)

    proc1 = Process(target=foo, args=(shm,))
    proc1.start()

    proc2 = Process(target=bar, args=(shm,))
    proc2.start()


    proc1.join()

    shm.close()
    shm.unlink()
