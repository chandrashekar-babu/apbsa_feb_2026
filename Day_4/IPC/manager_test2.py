from time import sleep
from multiprocessing import Process, Manager, Event


def foo(data, event):
    print("In foo: data =", data)
    for k, v in data.items():
        data[k] = v.upper()

    event.set()


def bar(data, event):
    print("In bar: data =", data)

    event.wait()
    for k, v in data.items():
        print(k, v)
    del data["city"]

#d = {}


if __name__ == '__main__':
    e = Event()

    m = Manager()
    d = m.dict()
    #d = dict()

    d["name"] = "Sam"
    d["city"] = "Mumbai"
    d["country"] = "India"

    p1 = Process(target=foo, args=(d, e))
    p2 = Process(target=bar, args=(d, e))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(d)
    print(type(d), d)

    #a = m.list()
    # a.append(10)
    # a.append(20)
    # print a, type(a)
