#from gevent import monkey; monkey.patch_all()

from time import sleep, time
from concurrent.futures import ThreadPoolExecutor as Executor
from queue import Queue

result = Queue()

def fetch_web_page(url):
    from urllib.request import urlopen
    try:
        print(f"Fetching {url}...")
        response = urlopen(url)
        print(f"Fetched {url}.")
    except HTTPError as e:
        r = (url, str(e))
    else:
        r = (url, str(response.code))
    
    result.put(r)
    return r

urls = [
    "http://www.chandrashekar.info/",
    "http://cisco.com/",
    "http://www.python.org/",
    "https://www.dhrona.net/",
    "http://www.kernel.org/",
    "http://www.debian.org/",
    "https://www.moonranger.net/"
]

if __name__ == '__main__':
    with Executor(max_workers=10) as workers:
        workers.map(fetch_web_page, urls)
        while True:
            print(result.get())