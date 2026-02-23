from threading import Thread
from time import sleep

def testfn(name, count, delay):
    print(f"Thread {name} started")
    
    for i in range(count):
        print(f"Thread {name} is running iteration {i+1}")
        sleep(delay)
    
    print(f"Thread {name} finished")

if __name__ == "__main__":
    t1 = Thread(target=testfn, args=("A", 10, 1))
    t2 = Thread(target=testfn, args=("B", 5, 1))

    t1.start()
    t2.start()

    t1.join(timeout=3)
    if t1.is_alive():
        print("main: Thread A is still running after 3 seconds, waiting for it to finish...")
    else:
        print("main: Thread A has finished, waiting for Thread B to finish...")

    t2.join(timeout=3)
    if t2.is_alive():
        print("main: Thread B is still running after 3 seconds, waiting for it to finish...")
        t2.join()  # Wait indefinitely until t2 finishes
    else:
        print("main: Thread B has finished.")

    #print("main: All threads have finished.")