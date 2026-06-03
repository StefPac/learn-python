import readchar
while True:
    key = readchar.readkey()
    if key.isalpha():
        print(chr(219 - ord(key.lower())), end="", flush=True)
    else:
        print(key, end="")