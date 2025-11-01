import random

# Assigning numeric values to represent each choice:
# 1 for Snake, -1 for Water, 0 for Gun
"""
Logic:
Snake drinks Water → Snake wins (1 beats -1)
Water douses Gun → Water wins (-1 beats 0)
Gun kills Snake → Gun wins (0 beats 1)
Same choice → Draw
"""

# Dictionary to map user input to numbers
youDict = {
    "s": 1,   # Snake
    "w": -1,  # Water
    "g": 0    # Gun
}

# Dictionary to convert numbers back to names (for printing)
reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

# Computer randomly chooses one of the three options
computer = random.choice([-1, 0, 1])

# Taking user input and converting it into the corresponding number
choice = input("Enter 's' for Snake, 'w' for Water and 'g' for Gun: ")
you = youDict[choice]

# Display both choices
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Checking all possible outcomes
if computer == you:
    # Same choice results in a draw
    print("It's a Draw! 🤐")
else:
    # Snake vs Water → Snake wins
    if computer == 1 and you == -1:
        print("You Lose! 🫤")
    elif computer == 1 and you == 0:
        print("You Win! 😁")

    # Water vs Snake → Snake wins
    elif computer == -1 and you == 1:
        print("You Win! 😁")
    elif computer == -1 and you == 0:
        print("You Lose! 🫤")

    # Gun vs Snake → Gun wins
    elif computer == 0 and you == 1:
        print("You Lose! 🫤")
    elif computer == 0 and you == -1:
        print("You Win! 😁")

    # Just in case something unexpected happens
    else:
        print("Something went wrong! 🚩")
