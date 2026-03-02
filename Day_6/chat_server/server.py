import socket
import threading
from protocol import send_msg, recv_msg

class ChatServer:
    def __init__(self, host='127.0.0.1', port=5000):
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_sock.bind((host, port))
        
        # State: { room_name: [list_of_sockets] }
        self.rooms = {} 
        # State: { socket: username }
        self.clients = {}
        
        self.state_lock = threading.Lock()

    def broadcast(self, room_name, message, sender_sock=None):
        with self.state_lock:
            if room_name in self.rooms:
                for sock in self.rooms[room_name]:
                    if sock != sender_sock:
                        try:
                            send_msg(sock, message)
                        except:
                            self.remove_client(sock)

    def remove_client(self, sock):
        with self.state_lock:
            name = self.clients.pop(sock, "Unknown")
            for room, members in self.rooms.items():
                if sock in members:
                    members.remove(sock)
                    self.broadcast(room, f"--- {name} has left the room ---")
            sock.close()

    def handle_client(self, sock, addr):
        print(f"[NEW CONNECTION] {addr}")
        current_room = None
        
        try:
            while True:
                raw_data = recv_msg(sock)
                if not raw_data: break
                
                cmd_parts = raw_data.split(' ', 1)
                cmd = cmd_parts[0].lower()

                if cmd == '/name':
                    name = cmd_parts[1] if len(cmd_parts) > 1 else "Anonymous"
                    with self.state_lock: self.clients[sock] = name
                    send_msg(sock, f"Name set to {name}")

                elif cmd == '/join':
                    new_room = cmd_parts[1] if len(cmd_parts) > 1 else "lobby"
                    with self.state_lock:
                        if new_room not in self.rooms: self.rooms[new_room] = []
                        self.rooms[new_room].append(sock)
                    current_room = new_room
                    self.broadcast(current_room, f"--- {self.clients.get(sock, 'User')} joined {new_room} ---")

                elif not cmd.startswith('/'):
                    if current_room:
                        msg = f"[{self.clients.get(sock, 'Guest')}]: {raw_data}"
                        self.broadcast(current_room, msg, sender_sock=sock)
                    else:
                        send_msg(sock, "Error: You must /join a room first.")
                
                elif cmd == '/close': break
        finally:
            self.remove_client(sock)

    def start(self):
        self.server_sock.listen()
        print("Server started on port 5000...")
        while True:
            conn, addr = self.server_sock.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()

if __name__ == "__main__":
    ChatServer().start()