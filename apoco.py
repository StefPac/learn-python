print("=" * 30)
print("     APOCO")
print("=" * 30)
print("""Day 1: Your alive and you know it. Do you want to:
        A.go to the store to get rations
        B.study the old book you found
      """)
answer1 = input(">")
if answer1 == "B":
    print("You open the book that you found the day before the apocolypes. you open the tome and read it's secrets. you learn a spell soul drain. You are hungry and head to the store.")
    print("You sprint down to the store and find that there is a zombie roaming around the entrence, you attack him with your bat, he falls to the ground. You collect some rations and leav the store. You are in need of a good book.")
    print("You sleep restlesly, Tomorow you shal find a new home.")
    print("""You see a treehouse and a tent.
          A.head to the treehouse
          B.head to the tent
          """)
    answer2 = input(">")
    if answer2 == "A":
        print("You head down to the treehouse and it is perfect. great choice")
        print("You win!!!")
    else:
        print("You head down to the tent. as soon as you enter a zombie awaits you. You cast soul drain but this monster is soulless.")
        print("💀GAME OVER💀")
else:
    print("You sprint down to the store and find that there is a zombie roaming around the entrence, you attack him with your bat, he falls to the ground. You collect some rations and leav the store. You are in need of a good book.")
    print("You open the book that you found the day before the apocolypes. you open the tome and read it's secrets. you learn a spell soul drain. You are hungry and head to the store.")
    print("You sleep restlesly, Tomorow you shal find a new home.")
    print("""You see a treehouse and a tent.
          A.head to the treehouse
          B.head to the tent
          """)
    answer2 = input(">")
    if answer2 == "A":
        print("You head down to the treehouse and it is perfect. great choice")
        print("You win!!!")