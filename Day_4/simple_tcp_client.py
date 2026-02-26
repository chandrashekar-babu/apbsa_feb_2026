from socket import socket, AF_INET, SOCK_STREAM
from time import sleep
from threading import Thread


def create_connection(n, hostname, port):
    print(f"Creating connection {n}")
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((hostname, port))
        outs = conn.makefile("w")
        for i in range(20):
            print(f"Connection {n}: count={i}")
            print(f"Connection {n}: count={i}", file=outs, flush=True)
            sleep(1)
        print("exit", file=outs, flush=True)

    finally:
        outs.close()
        conn.close()
            

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument("hostname")
    parser.add_argument("--port", type=int, default=9876)
    args = parser.parse_args()
        
    for i in range(2000):
        Thread(target=create_connection, args=(i+1, args.hostname, args.port)).start()


