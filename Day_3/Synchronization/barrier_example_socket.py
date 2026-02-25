from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN

from random import randint
from threading import Thread, current_thread, Barrier
from time import sleep
from random import randint

server_barrier = Barrier(2)
PORT = randint(6000, 8000)

def server():
    try:
        listener = socket(AF_INET, SOCK_STREAM)
        sleep(1)
        listener.bind(("127.0.0.1", PORT))
        listener.listen(SOMAXCONN)

        server_barrier.wait()
        client_conn = listener.accept()
        print("Got connection from ", client_conn)
        out = client_conn[0].makefile("w")
        out.write("Hello world from the server\n")
        out.close()
        client_conn[0].close()
    finally:
        listener.close()

def client():
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        server_barrier.wait()
        
        conn.connect(("127.0.0.1", PORT))

        instream = conn.makefile("r")
        line = instream.readline()
        print("Client: got message:", line)
        instream.close()
    finally:    
        conn.close()

if __name__ == '__main__':
    server_thread = Thread(target=server)
    client_thread = Thread(target=client)
    server_thread.start()
    client_thread.start()
