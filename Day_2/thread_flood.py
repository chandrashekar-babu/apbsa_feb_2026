# Do NOT run this code on Windows!
from gevent import monkey; monkey.patch_all()

from threading import Thread
import itertools

def testfn(i):
    from time import sleep
    print(f"testfn-{i} invoked")
    sleep(60)

if __name__ == '__main__':
    for i in itertools.count(1):
        t = Thread(target=testfn, args=(i,))
        t.start()
