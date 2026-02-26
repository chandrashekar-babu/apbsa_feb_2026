from multiprocessing import Process, Array, Event
from time import sleep

def foo(s, u):
    for i, v in enumerate(s):
        if s[i] >= 97:
            s[i] = s[i] - 32
    u.set()


def bar(s, u):
    u.wait()
    for i, v in enumerate(s):
        if s[i] == 32:
            s[i] = 10

if __name__ == '__main__':

    s = input("Enter a string: ")

    buf = Array('b', bytes(s, "utf8"))
    print(f"{buf=}")

    #buf = Array("u", s)
    #print(f"{buf=}")

    updated = Event()

    p1 = Process(target=foo, args=(buf, updated))
    p2 = Process(target=bar, args=(buf, updated))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Result buffer = ", str(bytes(buf), "utf8"))
