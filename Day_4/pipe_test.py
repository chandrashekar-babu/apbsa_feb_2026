from multiprocessing import Process, Pipe
from time import sleep

def testfn1(conn):
    conn.send("Hello, world")
    sleep(1)
    conn.send(100)
    sleep(1)
    conn.send([44, 55, 66, 77])
    sleep(1)
    conn.send({"name": "John Doe", "score": 97})
    sleep(1)


def testfn2(conn):
    while True:
        v = conn.recv()
        print(f"In testfn2: {v=}")
        print("-" * 30)


if __name__ == '__main__':
    c1, c2 = Pipe()
    p1 = Process(target=testfn1, args=(c1,))
    p2 = Process(target=testfn2, args=(c2,))

    p1.start()
    p2.start()
