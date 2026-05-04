import random
while True:
    print ("Insult me")
    roast = input ("Type your roast in hear, or are you to much of a weasle not to: ")
    insults = [
    "Your face has more bugs than the 2003 linux kernle!",
    "Evrey time you go to the doctors they order a scale larger than dark energy has expanded space!",
    "Look, there should be a indent in your code but instead there is a dent in your brain!",
    ]
    comeback = random.choice(insults)
    print(comeback)
    

