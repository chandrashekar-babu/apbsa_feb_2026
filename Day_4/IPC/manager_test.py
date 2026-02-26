from time import sleep
from multiprocessing import Process, Manager
#from threading import Thread as Process

def foo(data):
    print("In foo: name =", data["name"])
    print("In foo: value =", data["value"])

    data["name"] = "foo"
    data["value"] = 100

    print("In foo: name =", data["name"])
    print("In foo: value =", data["value"])

    sleep(1)
    print("In foo: name now is", data["name"])
    print("In foo: value now is", data["value"])

    sleep(1)
    print("In foo: name changed to", data["name"])
    print("In foo: value changed to", data["value"])
    print("In foo: new_value =", data["new_value"])

    print("Foo complete")



def bar(data):
    sleep(1)
    print("In bar: data[name] = ", data["name"])
    print("In bar: data[value] = ", data["value"])

    data["name"] = data["name"].upper()
    data["value"] = data["value"] * 100
    data["new_value"] = 600

    print("In bar: data[name] changed to", data["name"])
    print("In bar: data[value] changed to", data["value"])

    print("Bar complete")

if __name__ == '__main__':

    #d = {}

    m = Manager()
    d = m.dict()
    #l = m.list()

    d["name"] = "dummy"
    d["value"]= 200

    t1 = Process(target=foo, args=(d,))
    t2 = Process(target=bar, args=(d,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(dict(d), type(d))


    #p1 = Process(target=foo, args=(d,))
    #p2 = Process(target=bar, args=(d,))

    #p1.start()
    #p1.join()
    #print "After foo: name = %s, value = %d\n" % (d["name"], d["value"])

    #p2.start()
    #p2.join()
    #print "After bar: name = %s, value = %d\n" % (d["name"], d["value"])
