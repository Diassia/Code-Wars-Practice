# Create a function that takes an argument n and sums even fibonacci numbers upto n's index in the fibonacci sequence.

# Example:

# sum_fibs(5) == 2. (0, 1, 1, 2, 3, 5); 2 is the only number in the sequence and doesn't have another number in the sequence to get added to in the indexed fibbonacci sequence.
# Example:

# sum_fibs(9) == 44. (0, 1, 1, 2, 3, 5, 8, 13, 21, 34); 
# 2 + 8 + 34 = 44;

def sum_fibs(n):
    fibbonacci = []
    fibbonacci_calculation = 0
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

    for number in fibbonacci:
        if number % 2 == 0:
            fibbonacci_calculation += number
        else:
            continue

    return fibbonacci_calculation


print(sum_fibs(5))