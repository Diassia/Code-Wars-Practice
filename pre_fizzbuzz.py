# This is the first step to understanding FizzBuzz.

# Your inputs: a positive integer, n, greater than or equal to one. n is provided, you have NO CONTROL over its value.

# Your expected output is an array of positive integers from 1 to n (inclusive).

# Your job is to write an algorithm that gets you from the input to the output.

def pre_fizz(n):
    list = []
    for i in range(n):
        list.append(i + 1)
    return list

print(pre_fizz(10))

    # CodeWars Solution:
    # def pre_fizz(n):
    #     #your code here
    #     return list(range(1, n+1))