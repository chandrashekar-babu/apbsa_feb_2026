from socket import socket, AF_INET, SOCK_STREAM

def handle_connection(sock):
    with sock:
        ins, outs = sock.makefile("r"), sock.makefile("w")
        while True:
            incoming_message = ins.readline()
            if not incoming_message or incoming_message.strip().lower() == "exit":
                print("Server has closed the connection.")
                break
            print(f"Received from server: '{incoming_message.strip()}'")

            msg = input("Enter message: ")
            print(msg, file=outs, flush=True)

s = socket(AF_INET, SOCK_STREAM)
s.connect(('100.65.103.24', 12345))

handle_connection(s)

#ins = s.makefile("r")
#outs = s.makefile("w")

#msg = ins.readline()
#print(f"Received from server: '{msg}'")

#print("Got your message, server. This is the client.", file=outs, flush=True)

#s.close()
