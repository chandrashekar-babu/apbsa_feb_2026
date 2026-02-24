from multiprocessing import Process
from signal import signal, SIGTERM
from time import sleep

def foo():
    def term_handler(sig, frame):
        print(f"foo: term_handler invoked with signal = {sig}, frame = {frame}")
        exit(0)

    signal(SIGTERM, term_handler) 
    for i in range(10):
        print("foo: counting", i)
        sleep(2)   


def bar():
    def term_handler(sig, frame):
        print(f"bar: term_handler invoked with signal = {sig}, frame = {frame}")

    signal(SIGTERM, term_handler) 
    for i in range(10):
        print("bar: counting", i)
        sleep(2)   


if __name__ == '__main__':
    p1 = Process(target=foo)
    p2 = Process(target=bar)

    p1.start()
    p2.start()
    sleep(5)
    p1.terminate()  # os.kill(p1.pid, signal.SIGTERM)
    sleep(7)
    p2.kill()

    p1.join()
    p2.join()
