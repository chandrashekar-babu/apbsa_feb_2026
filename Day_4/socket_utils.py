from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from concurrent.futures import ThreadPoolExecutor as Executor

class TCPServer:
    def __init__(self, host='localhost', port=12345, handler=None, executor=None):
        self.host = host
        self.port = port
        self.handler = handler
        self.close = False
        self.executor = executor

    def start(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server listening on {self.host}:{self.port}")

    def serve_forever(self):
        if self.executor:
            with self.executor:
                while not self.close:
                    client_socket, addr = self.server_socket.accept()
                    print(f"Connection from {addr}")
                    self.executor.submit(self.handler, client_socket)
        else:
            while not self.close:
                client_socket, addr = self.server_socket.accept()
                print(f"Connection from {addr}")
                with client_socket:
                    if self.handler:
                        self.handler(client_socket)

    def shutdown(self):
        self.close = True
        self.server_socket.close()

    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shutdown()

if __name__ == "__main__":
    def echo_handler(client_socket):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            client_socket.sendall(data)

    with TCPServer(handler=echo_handler, executor=Executor(max_workers=4)) as server:
        server.serve_forever()