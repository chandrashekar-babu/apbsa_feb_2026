from multiprocessing import Process, current_process as current, Array
from time import sleep

arr = Array('i', [3, 2, 6, 8, 3, 1, 8, 5, 9, 4])

def update(arr):
    for i, v in enumerate(arr):
        arr[i] = v * v
        sleep(0.5)
            
def get_stats(arr):
    
    for _ in range(5):
        sleep(1)
        print(f'{current().name} - {arr[:]}')


if __name__ == '__main__':
    t1 = Process(target=update, args=(arr,))
    t2 = Process(target=get_stats, args=(arr,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()