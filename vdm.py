import time
print("=" * 20)
print("         VDM")
print("=" * 20)
mode = input("Fast or precise? ")
if mode == "fast":
    threshold = 30_860_000_000_000_000_000
    megaparcecs = 0
    timewrap = 31_500_000_000_000_000
    distance = 508_400_000_000_000_000_000
    hubble = 70
    velocity = 100_000_000_000_000_000_000
    print("Velocity: ", velocity)
    print("Distance: ", distance)
    while True:
        print("Target: M87 ")
        velocity = hubble * (distance // threshold)
        distance = distance + velocity * timewrap
        megaparcecs = distance // threshold
        print("Distance: ", distance, "| Megaparcecs: ", megaparcecs)
        print("Velocity", velocity, "kilomiters/second")
        time.sleep(1)
else:
    threshold = 30_860_000_000_000_000_000
    megaparcecs = 0
    timewrap = 1
    distance = 508_400_000_000_000_000_000
    hubble = 70
    velocity = 100_000_000_000_000_000_000
    print("Velocity: ", velocity)
    print("Distance: ", distance)
    while True:
        print("Target: M87 ")
        velocity = hubble * (distance // threshold)
        distance = distance + velocity * timewrap
        megaparcecs = distance // threshold
        print("Distance: ", distance, "| Megaparcecs: ", megaparcecs)
        print("Velocity", velocity, "kilomiters/second")
        time.sleep(1)
    