suswords = [
"um",
"IDK",
"how do you expect me to know that",
"maybe",
"thats personal"]
sus_score = 0
print("--interogattor---")
answer1 = input("Where were you on the night of the crime? ")
for word in suswords:
    if word in answer1:
        sus_score = sus_score + 1
answer2 = input("Do you own a weapon? ")
for word in suswords:
    if word in answer2:
        sus_score = sus_score + 1
answer3 = input("Who do you think did it? ")
for word in suswords:
    if word in answer3:
        sus_score = sus_score + 1
if sus_score >= 2:
    print("GUILTY")
else:
    print("INNOCENT")

