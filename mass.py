mass = int(input("What is the mass of the asteroid in kg? "))
print("Mass: ", mass)
speed = int(input("Speed in km/s"))
print("Speed: ", speed, "km/s")
speedms = speed * 1000
print("Speed in m/s: ", speedms)
en = 0.5 * mass * speedms ** 2
print("Enerergy: ", en, "jouls")

