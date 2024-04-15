import socket
from custom_string import CustomString

HEADER = 64
DISCONNECT_MSG = "!DISCONNECT"
SERVER = "172.20.10.2"
PORT = 8070


class Client:
    def __init__(self, server, port) -> None:
        self.cs = CustomString()
        self.servername = server
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.servername, self.port))
        while (True):
            message = input("Enter a message : ")
            if (message == DISCONNECT_MSG):
                self.send(DISCONNECT_MSG)
                break
            if (message):
                self.send(message)
            else:
                pass

    def send(self, msg: str):
        print("{CLIENT SIDE LOGS} : PACKING THE STRING")
        msg = self.cs.pack(msg).encode()
        length = str(len(msg)).encode()
        length += b' ' * (HEADER-len(length))
        self.client.send(length)
        self.client.send(msg)
        print("{CLIENT SIDE LOGS} : BIT STREAM SENT")


if __name__ == "__main__":
    Client(SERVER, PORT)
