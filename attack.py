import socket

server = socket.socket()
server.bind(("127.0.0.1", 5607))
server.listen()
while True:
    print ("🔥 COMMADABLE WRAITH ONLINE - scanning for intruders...")
    hacker, address = server.accept()
    print("🚨 INTRUDER DETECTED:", address)
    command = input("⚡️ command [1=BLOCK, 2=SCARE, 3=FAKE ERROR]: ")
    if command == "scare":
        hacker.send(b"You have been detected by the comet security team, prepare for prison")
    elif command == "2":
            hacker.send(b"You have been detected by the comet security team, prepare for prison")
    elif command == "1":
        hacker.send(b"ACCSESS_DENIED - SOTAS has cut your connection")
        hacker.close()
    elif command == "block":
         hacker.send(b"ACCSESS_DENIED - SOTAS has cut your connection")
         hacker.close()