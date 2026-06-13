from datetime import datetime
import random
import time
import socket 
memory = {}
while True:
    command = input(">")
    if command == "X.instal(soul)virus(H31qkill)": 
        xcommand = input(">")
        print("Xvirus_exit")
        time.sleep(5)
        exit()
    elif command == "stamp.stamp()":
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
        chars = '_-=";><()*^/!@#$%:?'
        for j in range(10):
            line = ""
            for i in range(30):
                line = line + random.choice(chars)
        print(line)
        print(line)
        print(line)
    elif command == "X.install(soul)drain.tool":
        message ="You will suffer pain even if proven innocent. Your soul has left you, you feel a pain in your forehead"
        for letter in message:
            print(letter, end="",flush=True)
            time.sleep(0.1)
            print()
    elif command.startswith("save.varb"):
        inside = command.split("[")[1].split("]")[0]
        parts = inside.split()
        memory[parts[0]] = parts[2]
        print("Inellismemory", parts[0], "=", parts[2])
    elif command.startswith("stamp.varb"):
        inside = command.split("[")[1].split("]")[0]
        print(memory[inside])