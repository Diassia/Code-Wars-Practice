# Your task is to create functionisDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.

# A few cases:


# (-12, 2, -6)  ->  true
# (-12, 2, -5)  ->  false

# (45, 1, 6)    ->  false
# (45, 5, 15)   ->  true

# (4, 1, 4)     ->  true
# (15, -5, 3)   ->  true

# Original code:
# def is_divide_by(number, a, b):
#     if (number % a == 0) and (number % b == 0):
#         return True
#     else:
#         return False

# My refactored code:
def is_divide_by(number, a, b):
    return (number % a == 0) and (number % b == 0)

number = -12
a = 2
b = -6

print(is_divide_by(number, a, b))