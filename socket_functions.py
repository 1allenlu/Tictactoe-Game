import socket

class socket_connection:

    def __init__(self, sk: socket.socket):
        '''initilize socket'''
        self.sk = sk
    
    def connect(self, address: str, port: int):
        '''try to connect to server by using address and port'''
        self.sk.connect((address, port))

    def wait_client(self, address: str, port: int):
        '''listen and accepts'''
        self.sk.bind((address, port))
        self.sk.listen()
        return self.sk.accept()

    def send_msg(self, msg: str):
        '''send message via socket'''
        self.sk.send(msg.encode("utf-8"))

    def recv_msg(self):
        '''receive message via socket'''
        return self.sk.recv(4096).decode("utf-8")
