import socket
import threading
from custom_string import CustomString

HEADER = 64
DISCONNECT_MSG = "!DISCONNECT"


cs = CustomString()


class Server:
    def __init__(self, hostname, port) -> None:
        self.hostname = hostname
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        print(f"[STARTING] Starting server on : {self.hostname}:{self.port} ")
        self.start()

    @staticmethod
    def handle_client(conn: socket.socket, addr):
        print(f"[NEW CONNECTION] {addr} connected.\n")
        connected = True
        while connected:
            try:
                length = int(conn.recv(HEADER).decode())
                msg = cs.unpack(conn.recv(length).decode())
                if (msg == DISCONNECT_MSG):
                    connected = False
                print(f"[{addr}] : {msg}")
            except Exception as e:
                pass
        conn.close()

    def start(self):
        self.socket.listen()
        while True:
            conn, addr = self.socket.accept()
            thread = threading.Thread(
                target=Server.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}.\n")


if __name__ == "__main__":
    Server(socket.gethostbyname(socket.gethostname()), 8070)
