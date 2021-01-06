# You are given num (up to 15 digits, never less than 0).

# If the length of num is even, return odd numbers as ints and even ones as strings, based on their position in the given number. Strings alternate in type cases: starting in lowercase to uppercase and so on based on position. If the length of num is odd, all the rules are opposite. See sample tests.

# Note: Positions of numbers are 1-based.

# if length of num is:
#   Even: return odd numbers as ints
#   strings alternate from lower to upper based on position (the number of letters = their position)
# if length of num is:
#   Odd: all rules are opposite

numbers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

def conv(num):
    number_string = str(num)
    string = ''
    position = 1

    if len(str(num)) % 2 == 0:
        for number in number_string:
            if int(number) == 0:
                for integer, num_string in numbers.items():
                    if integer == int(number):
                        string += num_string[:position]
                        position += 1
            elif int(number) % 2 == 0:
                for integer, string in numbers.items():
                    if integer == int(number):
                        string += string[:position]
                        position += 1
            else:
                position += 1
                string += number
    else:
        # for number in number_string:
        #     if int(number) == 0:
        #         for integer, num_string in numbers.items():
        #             if integer == int(number):
        #                 string += num_string[:position]
        #                 position += 1
        #     elif int(number) % 2 == 0:
        #         for integer, string in numbers.items():
        #             if integer == int(number):
        #                 string += string[:position]
        #                 position += 1
        #     else:
        #         position += 1
        #         string += number
        
        # for number in number_string:
        #     if int(number) == 0:

        return num

    # else:
    #     for number in num:


    return string


print(conv(0))
print(conv(1101))
print(conv(157953793516872))