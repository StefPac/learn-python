
import time
import socket 
while True:
    command = input(">")
    if command == "X.instal(soul)virus(H31qkill)": 
        xcommand = input(">")
        print("Xvirus_exit")
        time.sleep(5)
        exit()
    elif command == "stamp()":
        stamp = input(">")
        print(stamp)
    elif command == "send.message":
        msg = input(">")
        set1 = socket.socket()
        set1.connect(("127.0.0.1", 5400))
        set1.send(msg)
    