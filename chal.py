print("𑙩 Hyipnosis 🔗")
riddle = input("Solve this, what has 4 legs at dawn, 2 legs at noon, and 3 legs at the night")
if riddle == "human":
    print("CORRECT")
    with open("hyipno") as f:
       reader = f.read()
       print(reader)
else:
    exit()