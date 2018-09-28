import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1111))

print("Veuillez saisir vos logins")
msg = input(">> ")
s.send(msg.encode())
r = s.recv(9999999)
print(r.decode())

while True:
    msg = input(">> ")
    s.send(msg.encode())
    r = s.recv(9999999)
    print(r.decode())

