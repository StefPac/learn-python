password = input("password:")
if password == "3435":
    user_code = input("user code:")
    with open("banned") as f:
        banned = f.read()
        if user_code in banned:
            exit()
    print("---ASTROPHYISICS---")
    while True:
          with open("banned") as f:
            banned = f.read()
            if user_code in banned:
                exit()
            what = input("What do you want to learn today?")
            if what == "black holes":
                print("Black holes are areas where gravity is so strong evrything gets stuck in the super gravity whole, even light. matter, energy, and light can escape a black hole, evry time this happens, the black hole loses mass.")
            elif what == "dark energy":
                print("Dark energy is what expands our universe. Dark energy is in a constant tug-of-war with dark matter. Dark enegy feeds itself, for evry 31 quintillion kilomiters it expands the universe, it expands the uneverse 70 kilomiters faster")
            elif what == "dark matter":
                print("Dark matter is what keeps our uneverse from collapesing. planets orbiting stars would go so fast, they would fling off course, but dark matter provides gravity and stops this from happening.")
            elif what == "image1":
                print("""
    **********************************************
    **********************************************
    *************@@@@@****************************
    ************@-----@***************************
    ********@@@ /      \\@*************************
    *********@ / matter \\@@***********************      
    ********@@/          \\@@@********************
    ********@|            |@@*********************
    ******** @\\         /@@***********************
    **********@\\       /@*************************
    ************\\_____/ @@************************
    **********************************************    
    **********************************************          
    """)
            elif what == "admin":
                with open ("banned") as f:
                    banned = f.read()
                    if user_code in banned:
                        exit()
                admincode = input("enter the admin code")
                if  admincode == "Hawking":
                    print ("Welcome master")
                    write_banned = input("Would you like to remove anyone from the program today master?")
                    with open ("banned") as f:
                        banned = f.read()
                        if user_code in banned:
                            exit()
                            with open("banned", "a") as f:
                                f.write(write_banned + "\n")
            else:
                exit()    
else:
    exit()
