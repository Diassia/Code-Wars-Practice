# Instructions
# The goal of this kata is two-fold:

# 1.) You must produce a fibonacci sequence in the form of an array, containing a number of items equal to the input provided.

# 2.) You must replace all numbers in the sequence divisible by 3 with Fizz, those divisible by 5 with Buzz, and those divisible by both 3 and 5 with FizzBuzz.

# For the sake of this kata, you can assume all input will be a positive integer.

# Use Cases
# Return output must be in the form of an array, with the numbers as integers and the replaced numbers (fizzbuzz) as strings.

# Examples
# Input:

# fibs_fizz_buzz(5)
# Output:

# [ 1, 1, 2, 'Fizz', 'Buzz' ]
# Input:

# fibs_fizz_buzz(1)
# Output:

# [1]
# Input:

# fibs_fizz_buzz(20)
# Output:

# [1,1,2,"Fizz","Buzz",8,13,"Fizz",34,"Buzz",89,"Fizz",233,377,"Buzz","Fizz",1597,2584,4181,"FizzBuzz"]

def fizz_buzz(fibonacci):
    fb_fibonacci = []
    for number in fibonacci:
        if number % 3 == 0 and number % 5 == 0:
            fb_fibonacci.append('FizzBuzz')
        elif number % 3 == 0:
            fb_fibonacci.append('Fizz')
        elif number % 5 == 0:
            fb_fibonacci.append('Buzz')
        else:
            fb_fibonacci.append(number)
    return fb_fibonacci

def fibs_fizz_buzz(n):
    fibbonacci = []
    n1 = 0
    n2 = 0
    for i in range(n): #e.g. range of 10
        if i == 0:
            fibbonacci.append(i + 1)
            n1 = 1
        elif i == 1:
            fibbonacci.append(i)
            n2 = 1
        else:
            fib_no = n1 + n2
            fibbonacci.append(fib_no)
            #update values
            n1 = n2
            n2 = fib_no
    return fizz_buzz(fibbonacci)

n = 10

print(fibs_fizz_buzz(n))