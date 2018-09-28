import threading
import socket

class Server(threading.Thread):

    def __init__(self, clientsocket):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket

    def run(self):
        while True:
            r = self.clientsocket.recv(2048)
            self.clientsocket.send()

    def initConn(self):
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        tcpsock.bind(("", 1111))

        while True:
            tcpsock.listen(10)
            print("En écoute...")
            (clientsocket, (ip, port)) = tcpsock.accept()
            newthread = Server(clientsocket)
            newthread.start()