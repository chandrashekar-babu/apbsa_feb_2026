from multiprocessing import Process
from time import sleep


def testfn():
    from multiprocessing import current_process
    pname = current_process().name
    from itertools import count
    from signal import signal, SIGTERM, SIG_IGN

    def handler(signum, frame):
        print("Termination requested...")

    signal(SIGTERM, handler)
    signal(SIGUSR1, SIG_IGN)
    for i in count():
        print(f"{pname}: counting {i}")
        sleep(0.5)


if __name__ == '__main__':
    p = Process(target=testfn)
    p.start()
    sleep(5)
    p.terminate()
    sleep(2)

    import os
    import signal
    os.kill(p.pid, signal.SIGUSR1)
