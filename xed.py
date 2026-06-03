from datetime import datetime
import random
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
    elif command == "Hack(soul)drainint":

        print("draining📼")
        text = input(">")
        f = open("drained.txt", "a")
        f.write(text + "\n")
        f.close()
        time.sleep(3)
        exit()
    elif command == "time.check":
        print("Time:", datetime.now())
    elif command == "roll.dice()":
        print(random.randint(1, 20))
    elif command == "paint.opencanvas":
        chars = '_-=";><()*^/!@#$%:\?'
        for j in range(10):
            line = ""
            for i in range(30):
                line = line + random.choice(chars)
        print(line)