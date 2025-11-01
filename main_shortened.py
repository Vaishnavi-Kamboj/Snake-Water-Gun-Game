import random   # Importing random module to let the computer make random choices

"""
Assigning numerical values to each option:
1 for Snake
-1 for Water
0 for Gun
This helps us easily compare choices later using math instead of long if-else chains.
"""

# Dictionary to convert user input letters into corresponding numeric values
youDict = {
    "s": 1,    # Snake
    "w": -1,   # Water
    "g": 0     # Gun
}

# Reverse dictionary to convert numeric values back into words for display
reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

# Computer randomly chooses one among Snake(1), Water(-1), or Gun(0)
computer = random.choice([-1, 0, 1])

# Taking input from the user
choice = input("Enter 's' for snake, 'w' for water, and 'g' for gun: ")

# Converting user's choice into numeric form
you = youDict[choice]

# Displaying both choices
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Checking the result of the game
if computer == you:
    print("It's a Draw! 🤐")   # Both chose the same thing
elif computer - you == -1 or computer - you == 2:
    print("You Lose! 🫤")      # Conditions where computer wins
else:
    print("You Win! 😁")       # All other conditions mean you win

"""
Logic behind (computer - you == -1 or computer - you == 2):

We assigned:
Snake = 1, Water = -1, Gun = 0

So:
- Snake(1) vs Water(-1) → 1 - (-1) = 2 → Player wins
- Water(-1) vs Gun(0) → (-1) - 0 = -1 → Computer wins
- Gun(0) vs Snake(1) → 0 - 1 = -1 → Computer wins

Hence, whenever (computer - you) = -1 or 2 → Computer wins,
otherwise → You win.
"""
