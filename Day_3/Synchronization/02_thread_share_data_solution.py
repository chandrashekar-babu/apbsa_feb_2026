from threading import Thread, Lock

SIZE = 100_000

nums = list(range(SIZE))
nums_lk = Lock()

def pick_elements_buggy(dataset, howmany, result):
    for _ in range(howmany):
            nums_lk.acquire()  # Prone to deadlocks
            
            value = dataset[0]
            result.append(value)
            del dataset[0]
            
            nums_lk.release()

def pick_elements_legacy(dataset, howmany, result):
    for _ in range(howmany):
        try:
            nums_lk.acquire()  # Preferred for very old versions of Python (<= 2.4)
            
            value = dataset[0]
            result.append(value)
            del dataset[0]
        finally:
            nums_lk.release()

def pick_elements(dataset, howmany, result):
    for _ in range(howmany): 
        with nums_lk:
            value = dataset[0]
            result.append(value)
            del dataset[0]
        # result.append(dataset.pop())

if __name__ == '__main__':
    result1 = []
    result2 = []

    backup = nums.copy()

    t1 = Thread(target=pick_elements, args=(nums, SIZE//2, result1))
    t2 = Thread(target=pick_elements, args=(nums, SIZE//2, result2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("nums = ", nums)
    print(set(result1) & set(result2))
    print(set(backup) - (set(result1) | set(result2)))
    #print(f"{result1=}, {result2=}")
