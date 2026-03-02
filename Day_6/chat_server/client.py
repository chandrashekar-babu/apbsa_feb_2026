import socket
import threading
import sys
from protocol import send_msg, recv_msg

def receive_handler(sock):
    while True:
        try:
            msg = recv_msg(sock)
            if msg:
                print(f"\r{msg}\n> ", end="")
            else:
                break
        except:
            break
    print("\nDisconnected from server.")
    sys.exit()

def start_client():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 5000))

    # Thread to handle incoming messages
    threading.Thread(target=receive_handler, args=(client_sock,), daemon=True).start()

    print("Commands: /name <nick>, /join <room>, /close")
    try:
        while True:
            user_input = input("> ")
            send_msg(client_sock, user_input)
            if user_input == "/close":
                break
    except KeyboardInterrupt:
        pass
    finally:
        client_sock.close()

if __name__ == "__main__":
    start_client()