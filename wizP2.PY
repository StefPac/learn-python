import socket
import time
hp = 50

client = socket.socket()
client.connect(("127.0.0.1", 50350))
print("Conneced to game")
while True:
    print("P1:", question.decode())
    msg = input("You: ")
    client.send(msg.encode())
    reply = client.recv(1024)
    print("P1:", reply.decode())
    print("Soul drain(1)")
    print("firestorm(2)")
    print("ice shard(3)")
    spellcast = input("What spell do you want to cast: ")
    if reply.decode() == "Firestorm":
        hp = hp - 10
        print("Current health: ", hp)