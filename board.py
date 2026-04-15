print("========== THE BOARD ==========")
print("     SOTAS COMMAND CENTER")
print("===============================")
print("")
print("---LIST OF DARKNESS---")
darkness = {"45.33.32.156": "Russia", "185.220.101.1": "Germany", "8.8.8.8": "USA" }
for ip in darkness:
    print(ip, "->", darkness[ip])
print("")
wraith_status = input("Is the Hacker Wraith running? (yes/no): ")
print("---PRODUCT STATUS---")
if wraith_status == "yes":
    print("Hacker Wraith   :ONLINE")
else:
    print("Hacker Wraith   :OFFLINE")
scamera_status = input("Is the S-Camera running? (yes/no): ")
wraith_message = input("What should the wraith say to the hackers? ")
if wraith_message == "":
    wraith_message = "no change"
if scamera_status == "yes":
    print("S-Camera        : ONLINE")
else:
    print("S-Camera       : OFFLINE")
print("List Of Darkness : ACTIVE")
print("")
print("---WRAITH MESSAGE---")
print(wraith_message)
if wraith_message != "no change":
    f=open("wraith_msg.txt", "w")
    f.write(wraith_message)
    f.close()
    print("Wraith message UPDATED!")