from multiprocessing import Process, current_process as current
from multiprocessing.shared_memory import SharedMemory
import numpy as np
from time import sleep

def testfn1(a):
    a *= 2
    print(f"In testfn1[{current().name}]: a = {a}, {type(a)=}")

def testfn2(a):
    sleep(1)
    a **= 2
    print(f"In testfn2[{current().name}]: a = {a}, {type(a)=}")

if __name__ == '__main__':
    num_template = np.array([2, 3, 4, 5, 6])

    shm = SharedMemory(create=True, size=num_template.nbytes)

    nums = np.ndarray(num_template.shape, dtype=num_template.dtype, buffer=shm.buf)
    nums[:] = num_template

    print(f"In __main__[{current().name}]: nums = {nums}")

    #testfn1(nums)
    #testfn2(nums)
        
    p1 = Process(target=testfn1, args=(nums,))
    p2 = Process(target=testfn2, args=(nums,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    print(f"In __main__[{current().name}]: nums = {nums}")
    shm.close()
    shm.unlink()
    

