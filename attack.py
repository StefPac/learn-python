import socket

server = socket.socket()
server.bind(("127.0.0.1", 5000))
server.listen()
print ("🔥 COMMADABLE WRAITH ONLINE - scanning for intruders...")
hacker, address = server.accept()
print("🚨 INTRUDER DETECTED:", address)
