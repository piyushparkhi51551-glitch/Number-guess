import random

target=random.randint(1,100)
while True:
    userchoice = (input("Guess the target or Quit : "))
    if userchoice.lower() == "quit": 
        break

    userchoice=int(userchoice)
    if(userchoice == target):
        print("success : Correct Guess!!")
        break
    elif(userchoice < target):
        print("your number was too small. Take a bigger choice")    
    else:
        print("your number was too big. Take a smaller guess")

print("................Game over................")
