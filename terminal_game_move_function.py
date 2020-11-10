# In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice two times.

# Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.

# Example:
# move(3, 6) should equal 15

# def move(position, roll):
#     position_start = position
#     dice_roll = roll * 2
#     return position_start + dice_roll

#refactored code
def move(position, roll):
    return position + (roll * 2)

print(move(3, 6))