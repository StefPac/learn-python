import socket


server = socket.socket()
server.bind(("127.0.0.1", 5000))
server.listen()
print("SOTAS CHAT - waiting for agent...")
freind, address = server.accept()
while True:
   freind.send(b"Would you like to send a file? (yes/no) ")
   msg = freind.recv(1024)
   print("Agent says:", msg.decode())
   reply = input("You: ")
   freind.send(reply.encode())





