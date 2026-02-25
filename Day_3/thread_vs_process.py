from threading import Thread as Task, current_thread as current
from time import sleep

NUM_TASKS = 24

def testfn():
    task = current()
    print(f"testfn() called by {task.name}.")
    sleep(20)
    print(f"testfn() from {task.name} exiting.")

if __name__ == '__main__':
    workers = []
    for i in range(NUM_TASKS):
        task = Task(target=testfn)
        task.start()
        workers.append(task)

    for task in workers:
        task.join()

    print("main task complete.")
