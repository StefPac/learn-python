import socket


server = socket.socket()
server.bind(("127.0.0.1", 6000))
server.listen()
print("S CAMERA ARMED...watching for movement...")
while True:
    friend, address = server.accept()
    alert = friend.recv(1024)
    print("🚨 ALERT:", alert.decode())

