print("=" * 40)
print("       🔒VAULTKEEP ONLINE🔒")
print("=" * 40)
user = input("👤 USER ID: ")
if user == "leo":
    print("Welcome, leo. enter your password below.")
    password = input("PASSWORD: ")
    if password == "dfggg":
        print("Facial recognition beginning")
        print("Analysing....")
        facecode = input("Enter your facial recognition code: ")
        if facecode == "H31q":
            secret = open("d.txt").read()
            print(secret)
        else:
            exit()

else:
    exit()