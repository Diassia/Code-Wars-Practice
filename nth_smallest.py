# Task
# Given an array/list [] of integers , Find the Nth smallest element in this array of integers

# Notes
# Array/list size is at least 3 .

# Array/list's numbers could be a mixture of positives , negatives and zeros .

# Repetition in array/list's numbers could occur , so don't Remove Duplications .

# Input >> Output Examples
# nthSmallest({3,1,2} ,2) ==> return (2) 
# Explanation:
# Since the passed number is 2 , Then * the second smallest element in this array/list is 2*

def nth_smallest(arr, pos):
    arr.sort()
    return arr[pos - 1]

arr = [3, 1, 2]
pos = 2

print(nth_smallest(arr, pos))