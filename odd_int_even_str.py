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

def repeat_string(num_string, position, reverse_rules): # maybe include reverse option for flipped rules
    converted_string = ''

    if reverse_rules == True:
        lowercase = False
    else:
        lowercase = True

    while position > len(converted_string):
        if lowercase == True:
            converted_string += num_string
            lowercase = False
        else:
            converted_string += (num_string).upper()
            lowercase = True

    return converted_string[:position]

def conv(num):
    number_string = str(num)
    string = ''
    position = 1
    
    if len(str(num)) % 2 == 0:
        for number in number_string: # iterates through number string
            if int(number) % 2 == 0 or int(number) == 0:
                for integer, num_string in numbers.items(): # iterates through the dictionary for number
                    if integer == int(number):
                        reverse_rules = False
                        string += repeat_string(num_string, position, reverse_rules)
                        position += 1
            else:
                position += 1
                string += number

    else:
        for number in number_string:
            if int(number) % 2 == 0 or int(number) == 0:
                position += 1
                string += number
            else:
                for integer, num_string in numbers.items():
                    if integer == int(number):
                        reverse_rules = True
                        string += repeat_string(num_string, position, reverse_rules)
                        position += 1

    return string


print(conv(0)) # expect "0"
print(conv(1101)) # expect "11zer1"
print(conv(11)) # expect "11"
print(conv(56789456)) # expect "5si7eigh9fourFO5sixSIXsi"
print(conv(54563)) # expect "F4FIV6THREE"
print(conv(47309534)) # expect "f73zero953fourFOUR"
print(conv(34266262106)) # expect "T4266262ONEoneONE06"
print(conv(15795379351687)) # expect "15795379351sixSIXsixSIXeightEIGHTeig7"
print(conv(157953793516872)) # expect "OFISEVNINEFIVEfTHREEtSEVENseNINEnineTHREEthreFIVEfiveFIONEoneONEon68SEVENsevenSEVE2"