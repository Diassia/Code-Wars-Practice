# Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots. i.e.

# 1st (1)   2nd (3)    3rd (6)
# *          **        ***
#            *         **
#                      *
# You need to return the nth triangular number. You should return 0 for out of range values:

#   triangular(0)==0,
#   triangular(2)==3,
#   triangular(3)==6,
#   triangular(-10)==0

# def triangular(n):
#     if n == 10:
#         return 55
#     if n <= 0:
#         return 0
#     else:
#         return n + triangular(n - 1)

def triangular(n):
    if n <= 0:
        return 0
    total = 0
    for i in range(n + 1): # e.g. range(5) = [0,1,2,3,4] - which doesn't include 5 for the triangular number hence n+1 (aka. range(6))
        total += i
    return total

print(triangular(2))
print(triangular(4))
print(triangular(9))
print(triangular(-9))
print(triangular(1000))


#factorial functions
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(1))
# print(factorial(4))
# print(factorial(7))