import socket

bad_ips = ["192.169.1.100", "10.0.0.5"]


server = socket.socket()
server.bind(("127.0.0.1, 5000"))
server.listen()

print("waiting for a freind...")

freind, address = server.accept()
ip = address[0]


if ip in bad_ips:
    print("BLOCKED:", IP)
    freind.close()
else:
    mnessage = freind.reciv(1024)
    print ("allowed:", ip, "says:", message.decode())
    freind.close()

server.close()
