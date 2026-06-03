import math
h0 = 70
matter = 0.31
darkenergy = 0.68 
w0 = -0.7
wa = -1
a = float(input("How big was the universe back then? (1 = today, smaller = longer ago)? "))
w = w0 + wa * (1-a)
de_push = 1 + 3 * w
print("Dark energy's push at that time:", de_push)
