def foo(x, y):
    print "In foo, x =", x, "y =", y


def bar(f, args):
    f(*args)


bar(foo, args=(10, 20))

