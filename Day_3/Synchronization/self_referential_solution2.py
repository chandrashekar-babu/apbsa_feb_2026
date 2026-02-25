from threading import RLock as Lock

stats = {
    "count": 0,
    "bcount": 0
}

stats_lock = Lock()

def bar():
    print("In bar function...")
    with stats_lock:
        stats["bcount"] += stats["count"]

def foo():
    print("In foo function...")
    with stats_lock:
        stats["count"] += 1
        bar()

foo()
print("foo complete...")