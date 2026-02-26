from multiprocessing import Process, current_process as current, Value
from time import sleep

stats = {
    'visits': Value('i', 0),
    'duration': Value('d', 0.0)
}

def update(stats):
    for _ in range(10):
        sleep(0.5)
        stats['visits'].value += 1
        stats['duration'].value += 0.5
        print(f"""update: {current().name} is running: 
              Visits = {stats["visits"].value}, 
              Duration = {stats["duration"].value}""")
    
def get_stats(stats):
    
    for _ in range(5):
        sleep(1)
        
        print(f"""-------------------------------
                get_stats: {current().name} is running: 
                  Visits = {stats["visits"].value}, 
                  Duration = {stats["duration"].value}
                -------------------------------""")


if __name__ == '__main__':
    t1 = Process(target=update, args=(stats,))
    t2 = Process(target=get_stats, args=(stats,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()