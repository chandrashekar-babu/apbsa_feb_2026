from multiprocessing import Process
from time import sleep

def testfn():

    def cleanup(*args, **kwargs):
        print(f"cleanup invoked: {args=}, {kwargs=}")
        exit(0)

    from signal import signal, SIGTERM
    signal(SIGTERM, cleanup)

    for i in range(20):
        print(f"testfn: counting {i}")
        sleep(1)


p1 = Process(target=testfn)
p1.start()

sleep(5)
p1.terminate()
