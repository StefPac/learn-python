import time
blood = 100
start = time.time()
input("Press to late and see what happens...")
end = time.time()
bloodlost = end - start
blood = blood - bloodlost + 15 - bloodlost
if blood <= 0:
    print("Game over, too much blood lost.")
else:
    print("Blood level: ", blood)