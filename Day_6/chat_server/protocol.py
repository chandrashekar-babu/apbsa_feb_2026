import socket
import struct

def send_msg(sock, msg_str):
    # Encode message to bytes
    data = msg_str.encode('utf-8')
    # Pack the length of data into 4 bytes (Network byte order)
    header = struct.pack('!I', len(data))
    sock.sendall(header + data)

def recv_msg(sock):
    # Read the 4-byte header
    header = sock.recv(4)
    if not header:
        return None
    msg_len = struct.unpack('!I', header)[0]
    # Read exactly msg_len bytes
    data = b''
    while len(data) < msg_len:
        packet = sock.recv(msg_len - len(data))
        if not packet:
            return None
        data += packet
    return data.decode('utf-8')