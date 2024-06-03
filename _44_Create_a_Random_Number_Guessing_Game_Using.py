import random
Cnumber = random.randrange(1,101)

userInput=int(input("Enter your number = "))
if userInput>Cnumber:
    print("Your guess number is high")
    print("computer number", Cnumber)
elif Cnumber>userInput:
    print("computer number", Cnumber)
    print("Your guess number is too low ")
else:
    print("computer number", Cnumber)
    print("Your guess number is equal")