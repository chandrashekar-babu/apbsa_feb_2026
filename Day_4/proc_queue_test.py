from multiprocessing import Process, Queue
from time import sleep



def testfn1(q):
    #q.put("Hello, world")
    #sleep(1)
    q.put(100)
    sleep(1)
    #q.put([44, 55, 66, 77])
    #sleep(1)
    #q.put({"name": "John Doe", "score": 97})
    #sleep(1)


def testfn2(q):
    while True:
        v = q.get()
        print(f"In testfn2: {v=}")
        print("-" * 30)


if __name__ == '__main__':
    q = Queue(10)
    p1 = Process(target=testfn1, args=(q,))
    p2 = Process(target=testfn2, args=(q,))

    p1.start()
    p2.start()
