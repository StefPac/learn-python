q = input("KM/LY or LY/KM? ")    
if q == "LY/KM":
    lightyears = int(input("How many light-years? "))
    km = lightyears * 9_460_000_000_000
    print(lightyears, "light-years = ", km, "km")
else:
    kmq = int(input("How many kilometers? "))
    kmm = kmq / 9_460_000_000_000
    print(kmq, "km = ", kmm, "light-years")