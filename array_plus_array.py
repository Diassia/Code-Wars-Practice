# I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their elements. I'll appreciate for your help.

# P.S. Each array includes only integer numbers. Output is a number too.

# First attempt:
# def array_plus_array(arr1, arr2):
#     sum_array1 = sum(arr1)
#     sum_array2 = sum(arr2)
#     total = sum_array1 + sum_array2
#     return total

# Refactored attempt
def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

print(array_plus_array(arr1, arr2))

# CodeWars solution:
#     def array_plus_array(arr1, arr2)
#         return sum(arr1 + arr2)