import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1111))

print("Le nom du fichier que vous voulez récupérer:")
while True:
    msg = input(">> ")
    s.send(msg.encode())
    r = s.recv(9999999)
