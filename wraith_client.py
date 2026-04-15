import socket

client = socket.socket()
client.connect(("127.0.0.1", 5000))
reply = client.recv(1024)
print(reply.decode())