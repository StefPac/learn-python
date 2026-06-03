state = "IDLE"
print("🎯The turret online - state:", state)
command = input("> ")
print("You said:", command)
if command == "move":
    state = "Moving"