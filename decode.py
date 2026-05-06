while True:
    key = int(input("key:"))
    coded = input("What message would you like to decode? ")
    decoded = ""
    for letter in coded:
        decoded = decoded + chr(ord(letter) - key)
        print(decoded)