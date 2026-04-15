import socket


client = socket.socket()
client.connect(("127.0.0.1", 5000))
print("Conneced to SOTAS chat")
question = client.recv(1024)
print("SOTAS:", question.decode())
msg = input("You: ")
client.send(msg.encode())
reply = client.recv(1024)
print("SOTAS:", reply.decode())