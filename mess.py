import random
paranoia = ["Someones behind you", "Look up stairs", "I know where you live", "Prepare for death"]
while True:
    para = random.choice(paranoia)
    print(para)
    feel = input("how do you feel now humble being? ")
    no =["No you do not feel {feel} it is just the feeling of the endless void.", "That is not {feel}, thats just the pain of your humble soul leaving you", "No, you feel hopeless, staring at the screen"]
    gaslight = random.choice(no)
    print (gaslight.format(feel=feel)) 