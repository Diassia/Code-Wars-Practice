    # input number, e.g. 10
    # want to add (num, e.g. 10) numbers numerically
    # e.g. 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    # start at 1 then add 1 each time up till num?

def summation(num):
    list_of_numbers = []
    for number in range(num):
        new_number = number + 1
        list_of_numbers.append(new_number)
    calculation = sum(list_of_numbers)
    return(calculation)

summation(10)
summation(500)
summation(8)
summation(22)
