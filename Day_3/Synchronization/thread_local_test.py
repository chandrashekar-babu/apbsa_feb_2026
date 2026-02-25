from threading import Thread
import threading
from time import sleep

data = threading.local()

class MyData: pass

#data = MyData()
#data.i = 10


def testfn1():

    #print("In testfn1:", data, data.i)
    data.i = 100
    sleep(1)
    print("In testfn1:, data.i =", data.i)

def testfn2():
    sleep(0.5)
    #print("In testfn2:", data, data.i)
    data.i = 200
    sleep(1)
    print("In testfn2:, data.i =", data.i)

if __name__ == '__main__':
    t1 = Thread(target=testfn1)
    t2 = Thread(target=testfn2)

    data.i = 1000
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("In main: data.i =", data.i)