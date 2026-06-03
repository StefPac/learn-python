import readchar
while True:
    key = readchar.readkey()
    haunt = {"l": "v", "n": "m", "x": " ", "b": "q", "w": "e", "g": "j" }
    if key in haunt:
        print(haunt[key], end="", flush=True)
    else:
        print(key)