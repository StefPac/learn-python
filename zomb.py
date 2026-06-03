import os
print("ZOMBIE KILL ONLINE...")
os.system("lsof -i :5060")
pid = input("Enter PID to kill: ")
os.system("kill"  + pid)