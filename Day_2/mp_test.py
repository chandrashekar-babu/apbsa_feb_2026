from multiprocessing import Process, current_process


def testfn():
    p = current_process()
    print(f"testfn: process name={p.name}, pid={p.pid}")

if __name__ == "__main__":
    p1 = Process(target=testfn, name="testfn_process_1")
    p2 = Process(target=testfn, name="testfn_process_2")
    p1.start()
    p2.start()

    testfn()

    