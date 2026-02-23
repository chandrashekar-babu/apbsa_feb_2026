import gevent

def foo():
    for i in range(10):
        print(f"In foo: counting {i}")
        gevent.sleep(1)

def bar():
    for i in range(10):
        print(f"In bar: counting {i}")
        gevent.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(foo)
    g2 = gevent.spawn(bar)
    print(g1, g2)
    gevent.joinall([g1, g2])
