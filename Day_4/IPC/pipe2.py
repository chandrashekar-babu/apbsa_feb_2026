from multiprocessing import Process, Pipe

class Car:
    def __init__(self, name):
        self.name = name

    def __str__(self): return "Car object, name = %s" % self.name


def foo(outbox, inbox):
    outbox.send([10, 20, 30, 40])

    result = inbox.recv()
    print("foo: got result -> {}".format(str(result)))

    outbox.send([ x / 2 for x in result])
    result = inbox.recv()
    print("foo: got result -> {}".format(str(result)))


def bar(outbox, inbox):
    data = inbox.recv()
    print("bar: received data -> {}".format(str(data)))
    outbox.send([x*x for x in data ])

    data = inbox.recv()
    print("bar: received data -> {}".format(str(data)))
    outbox.send([ x * 2 for x in data ])



w1, r1 = Pipe()
w2, r2 = Pipe()

p1 = Process(target=foo, args=(w1, r2,))
p2 = Process(target=bar, args=(w2, r1,))

p1.start()
p2.start()






