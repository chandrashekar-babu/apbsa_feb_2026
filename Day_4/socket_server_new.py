from gevent import monkey; monkey.patch_all()  # Patch standard library for cooperative multitasking
from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN, SOL_SOCKET, SO_REUSEADDR
from threading import Thread, current_thread as current
from concurrent.futures import ThreadPoolExecutor as Executor

def handle_connection(client_socket):
    with client_socket:
        ins, outs = client_socket.makefile("r"), client_socket.makefile("w")
        print("Welcome to the server!", file=outs, flush=True)

        while True:
            incoming_message = ins.readline()
            if not incoming_message or incoming_message.strip().lower() == "exit":
                print("Client has disconnected.")
                break

            print(f"{current().name}: Received from client: '{incoming_message.strip()}'")
            print(f"Reply: '{incoming_message.strip().upper()}'", file=outs, flush=True)


with socket(AF_INET, SOCK_STREAM) as s:
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('100.65.103.24', 12345))
    s.listen(SOMAXCONN) # SOMAXCONN is a constant that specifies the maximum number of queued connections. 
                        # It is typically set to a large value, such as 128 or 256, depending on the operating system.

    print("Server is listening on port 12345...")
    with Executor(max_workers=10_000) as executor:
        while True:
            client_socket, client_address = s.accept()
            print(f"Connection from {client_address} has been established.")
            executor.submit(handle_connection, client_socket)

        #client_socket.send(b"Welcome to the server!") 
        # socket.send() method is a low-level method that sends bytes data to the client.
        # It does not handle any protocol-specific details, such as message framing or encoding.
        # If you want to send a string message, you need to encode it to bytes before sending it.
        # For example, you can use the encode() method of a string to convert it to bytes:
        # message = "Welcome to the server!"


    #    outs = client_socket.makefile("w") 
        # makefile() method creates a file-like object that can be used to read and write data to the socket.

    #    ins = client_socket.makefile("r")
        # The "r" mode indicates that the file-like object is opened for reading, while

    #    outs.write("Welcome to the server!\n")
    #    outs.flush()  # Ensure the message is sent immediately
    #    print("This message is from the server.", file=outs, flush=True)

    #    reply = ins.readline()
    #    print(f"Received from client: '{reply}'")

    #    client_socket.close()
        #Thread(target=handle_connection, args=(client_socket,)).start()
        # Fork-on-demand is a technique where a new process or thread is created to handle each incoming connection.
        # This allows the server to handle multiple clients concurrently without blocking the main server thread.
        # But this is not scalable.
        
           