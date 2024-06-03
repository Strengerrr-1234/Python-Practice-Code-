import random
l = ["rock","scissor","paper"]

while True:
    computer_Count = 0
    User_Count =0
    userinput =int(input('''
        Game Start 
        1 yes
        2 No | Exit
            '''))
    if userinput == 1:
        for  a in range(1,6):
            UserInput = int(input('''
            1 Rock
            2 Scissor
            3 Paper  
            '''))
            if UserInput == 1:
                userchoice ="rock"
            elif UserInput == 2:
                userchoice ="Scissor"
            elif UserInput == 3  :
                userchoice = "Paper"
            ComputerChoice = random.choice(1)
            if ComputerChoice == userchoice:
                 print("Userchoice",userchoice)
                 print("ComputerChoice",ComputerChoice)
                 print("Game Draw")
                 User_Count = User_Count + 1
                 computer_Count = computer_Count + 1
            elif (userchoice=="Rock" and ComputerChoice=="Scissor") or (userchoice=="Paper" and ComputerChoice=="Rock") or (userchoice=="Scissor" and ComputerChoice=="Scissor"):
                print("Userchoice", userchoice)
                print("ComputerChoice", ComputerChoice)
                print("You Win")
                User_Count = User_Count+1
            else:
                print("Userchoice", userchoice)
                print("ComputerChoice", ComputerChoice)
                print("Computer  Win")
                computer_Count = computer_Count+1
        if User_Count == computer_Count:
            print("Final Game Draw ....")
            print("User score ", User_Count)
            print("Computer score",computer_Count)
        elif User_Count>computer_Count:
            print("Final YOu win the game ")
            print("User count",User_Count)
            print("computer score",computer_Count)
        else:
            print("final computet win the game")
            print("User score",User_Count)
            print("Computer score",computer_Count)
    else:
        break;
