from socket import socket, AF_INET, SOCK_STREAM

connections = []
for i in range(10_000):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('100.65.103.24', 12345))
    connections.append(s)
    print(f"Connection {i} established.")
    
