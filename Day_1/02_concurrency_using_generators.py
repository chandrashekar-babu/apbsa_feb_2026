from time import sleep

def foo():
    for i in range(10):
        print(f"In foo: counting {i}")
        yield
        sleep(1)

def bar():
    for i in range(10):
        print(f"In bar: counting {i}")
        yield
        sleep(1)

if __name__ == '__main__':
    g1 = foo()
    g2 = bar()
    for _ in zip(g1, g2): pass
