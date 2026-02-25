from threading import Thread, current_thread
from queue import Queue
from time import sleep

q = Queue(5)

def fetch_item():
    t = current_thread()
    sleep(1)
    print(f"{t.name}: fetching an element...")
    v = q.get()
    print(f"{t.name}: fetched item: {v}")
    q.task_done()


if __name__ == '__main__':
    workers = []
    for i in range(5):
        w = Thread(target=fetch_item)
        w.start()
        workers.append(w)
    
    print("Created 5 threads....")
    for v in range(10, 40, 10):
        print(f"Adding item: {v}")
        q.put(v)
    
    print("Added 3 items...")
    q.join()
    print("Got acknowledgement from all threads")
