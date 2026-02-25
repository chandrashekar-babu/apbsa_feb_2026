from random import randint, random
from threading import Thread, current_thread, Barrier
from time import sleep


class Data(Barrier, dict):
    def random_fill(self):
        th_name = current_thread().name
        for i in range(20):
            v = random()
            self[f"{th_name}-{i}"] = v
            sleep(v)
            print(".", end=" ", flush=True)
        print(" done.", flush=True)

    def read_data(self):
        th_name = current_thread().name
        data_str = bytearray(th_name, encoding="utf8")
        for v in self.values():
            data_str += b" {}".format(v)
            sleep(random())
        return str(data_str, encoding="utf8")


class DummyServer(Thread):

    def __init__(self, data, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self.data = data

    def start_server(self):
        print("Starting server.", end="", flush=True)
        self.data.random_fill()

    def run(self):
        self.start_server()
        self.data.wait()
        print("Server read: ", self.data.read_data())
        self.data.wait()


class DummyClient(Thread):
    def __init__(self, data, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self.data = data

    def connect_to_server(self):
        print(f"{self.name}: Connecting to server....", flush=True)
        self.data.wait()
        print(f"{self.name}: Connected to server....")

    def get_server_data(self):
        th_name

    def run(self):
        self.connect_to_server()
        self.get_server_data()


msg_barrier = Barrier(10)


def random_sleep_and_print():
    thread_name = current_thread().name
    v = randint(2, 10)
    sleep(v)
    msg_barrier.wait()
    print(f"{thread_name}: Woke up!")


if __name__ == '__main__':
    threads = {}
    for i in range(10):
        threads[i] = Thread(target=random_sleep_and_print)
        threads[i].start()
