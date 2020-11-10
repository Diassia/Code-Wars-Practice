# You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.

# Let's look at a few examples:

# array = [1, 2, 3, 4] and N = 2, then the result is 3^2 == 9;
# array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

def index(array, n):
    # try:
    #     if n > array[n]:
    #         return -1
    # except IndexError:
    #     return -1
    if n > len(array): # will check in 'n' is larger than the length of the array
        return -1
    result = array[n]**n
    return result

# array = [1, 2, 3, 4]
array = [1, 3, 10, 100]
n = 0

print(index(array, n))