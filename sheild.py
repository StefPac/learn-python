message = "Leo is the G.O.A.T"
coded = ""
for letter in message:
    coded = coded + chr(ord(letter) + 3)
print(coded)


decoded = ""
for letter in coded:
    decoded = decoded + chr(ord(letter) - 3)
print(decoded)

