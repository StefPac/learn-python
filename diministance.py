import math
print("DIMINISTANCE")
h0 = 70
matter = 0.31
darkenergy = 0.68 
w0 = -0.7
wa = -1
a = float(input("How big was the universe back then? (1 = today, smaller = longer ago)? "))
curvature = int(input(" How curved is the universe the lower the number the more sphere looking the universe is, the higher the number the more saddle looking the universe is?"))
w = w0 + wa * (1-a)
totalpush = matter / a**3 + darkenergy * (1 + 3 * w)
print("The whole universes push at that time: ", totalpush)
h = h0 * math.sqrt(matter / a**3 + darkenergy - curvature / a**2)
print("The universe was expanding at", h, "km/s/Mpc")