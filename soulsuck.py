import random
import time
message = "Your soul is mine. You feel a sharp pain in your chest, feel in pain, emotionless"
lett = "abcdefghijklmnopqrstuvwxyz"
scramb = ""
rev = 0
while rev <= len(message):
    line = message[:rev]
    for letter in message[rev:]:
        line = line + random.choice(lett)
    print(line)
    time.sleep(0.3)
    rev = rev + 1