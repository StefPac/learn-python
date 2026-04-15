import socket

server = socket.socket()
server.bind(("127.0.0.1", 5000))
server.listen()
print("HACKER WRAITH ONLINE...")
darkness = {"45.33.32.156": "Russia", "185.220.101.1": "Germany", "8.8.8.8": "USA" }
while True:
    freind, address = server.accept()
    ip = address[0]
    if ip in darkness:
        f = open("wraith_msg.txt", "r")
        scary = f.read()
        f.close()
        freind.send(scary.encode())
    else:
        freind.send(b"WELCOME FRIEND")