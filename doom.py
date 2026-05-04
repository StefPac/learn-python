import random
name = input("What is your name")
fave_book = input("What it is your favroit book: ")
great_fear = input("What is your greatest fear? ")
astrology_mark = input("what is your astrology sign")
death_cause = random.choice([fave_book, great_fear])
print(f"you will be killed by {death_cause}.")
