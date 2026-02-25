from concurrent.futures import ThreadPoolExecutor

def slow_square(x):
    from time import sleep
    sleep(1)
    return x*x

#result = map(slow_square, list(range(10)))
#print(list(result))

with ThreadPoolExecutor(max_workers=10) as executor:
    result = executor.map(slow_square, list(range(10)))
    print(list(result))

