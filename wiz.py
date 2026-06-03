import socket
hp = 50
print("⚡️ THE WIZARD GAMES ⚡️")
startgame = input("Would you like to host a game? (yes/no): ")
if startgame == "yes":
    network = socket.socket()
    network.bind(("127.0.0.1", 50350))
    network.listen()
    print("Waiting for players")
    friend, address = network.accept()
    print("P1 health points:", hp)
    friend.send(b"Would you like to join the game? (yes/no) ")
    msg = friend.recv(1024)
while True:
   print("Soul drain(1)")
   print("firestorm(2)")
   print("ice shard(3)")
   print("P2:", msg.decode())
   reply = input("You: ")
   friend.send(reply.encode())

