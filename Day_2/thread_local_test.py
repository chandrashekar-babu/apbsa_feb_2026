from threading import Thread
import threading
from time import sleep


class Local():
    pass

#a = Local()

a = threading.local()


def testfn1():

    print("In testfn1: setting a.value to 100")
    a.value = 100
    sleep(4)
    print("In testfn1: a.value =", a.value)

def testfn2():

    sleep(1)
    print("In testfn2: setting a.value to 200")
    a.value = 200
    sleep(1)
    print("In testfn2: a.value =", a.value)

if __name__ == '__main__':
    t1 = Thread(target=testfn1)
    t2 = Thread(target=testfn2)
    t1.start()
    t2.start()
        

