from threading import RLock as Lock

stats = {
    "cpu": 40,
    "mem": 30,
    "count": 0
}

stats_lock = Lock()

def update_cpu_usage():
    with stats_lock:
        stats["cpu"] += 5


def update_mem_usage():
    with stats_lock:
        stats["mem"] += 5

def update_stats():
    with stats_lock:
        update_cpu_usage()
        update_mem_usage()
        stats["count"] += 1

if __name__ == '__main__':
    update_stats()
