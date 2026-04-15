import socket


client = socket.socket()
client.connect(("127.0.0.1", 6000))
client.send(b"MOVEMENT DETECTED AT FRONT DOOR")