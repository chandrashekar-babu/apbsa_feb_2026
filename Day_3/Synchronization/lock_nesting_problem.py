from threading import Thread, Lock as Lock

stats = {
  "foo": 0,
  "bar": 0
}

stats_lock = Lock()


def bar():
    print(f"bar being invoked: {stats_lock=}")
    with stats_lock:
        print("bar in critical section...")
        stats["bar"] += 1

def foo():
    with stats_lock:
        print("foo in critical section..")
        bar()
        stats["foo"] += 1


if __name__ == '__main__':
    t = Thread(target=foo)
    t.start()
    t.join()
    print("program completed...")