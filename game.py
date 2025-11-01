import random
"""
1 for snake
-1 for water
0 for gun
"""

youDict = {"s" : 1,
           "w" : -1,
           "g" : 0
           }
reverseDict = {
    1:"Snake",
    -1: "Water",
    0 : "Gun"
}
computer = random.choice([-1,0,1])
choice = input("Enter 's' for snake,'w' for water and 'g' for gun : ")
you = youDict[choice]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if computer == you :
    print("It's a Draw!🤐")
else:
    if computer == 1 and you == -1:
        print("You Lose!🫤")
    elif computer == 1 and you == 0:
        print("You Win!😁")
    elif computer == -1 and you == 1:
        print("You Win!😁")
    elif computer == -1 and you == 0:
        print("You Lose!🫤")
    elif computer == 0 and you == 1:
        print("You Lose!🫤")
    elif computer == 0 and you == -1:
        print("You Win!😁")
    else:
        print("Something went wrong!🚩")