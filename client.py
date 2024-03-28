import socket

HEADER = 64
DISCONNECT_MSG = "!DISCONNECT"
SERVER = "172.20.10.2"
PORT = 8070


class Client:
    def __init__(self, server, port) -> None:
        self.servername = server
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.servername, self.port))
        self.send("Hello GUYS!")

    def send(self, msg: str):
        print("SENDING")
        msg = msg.encode()
        length = str(len(msg)).encode()
        length += b' ' * (HEADER-len(length))
        self.client.send(length)
        self.client.send(msg)
        print("SENT")


if __name__ == "__main__":
    Client(SERVER, PORT)
