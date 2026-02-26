from multiprocessing import Process, Pipe


class Car:
    def __init__(self, name):
        self.name = name

    def __str__(self): return "Car object, name = %s" % self.name


def sender(p):
    p.send(10)
    p.send(["john", "sam", 45.66])
    p.send(Car(name="Honda"))


def receiver(p):
    print(p.recv())
    print("-" * 40)
    print(p.recv())
    print("-" * 40)
    print(p.recv())
    print("-" * 40)

if __name__ == '__main__':
    write_end, read_end = Pipe()
    print(write_end, read_end)
    #print(dir(write_end))
    #del write_end.recv

    p1 = Process(target=sender, args=(write_end,))
    p2 = Process(target=receiver, args=(read_end,))

    p1.start()
    p2.start()
