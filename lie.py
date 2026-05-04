import random
print("---LIE DETECTOR---")
while True:
    question = input("ENTER STATEMENT HERE: ")
    print("ANALYZING...")
    verdict = ["TRUTH", "LIE"]
    ifnot = random.choices(verdict, weights=[20, 80])[0]
    print(ifnot)