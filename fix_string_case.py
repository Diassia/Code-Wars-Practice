# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
# For example:

# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

def lower_upper_convertion(case, s):
    conversion_string = ''
    for character in s:
        if case == 'lower' and not character.islower():
            conversion_string += character.lower()
        elif case == 'upper' and not character.isupper():
            conversion_string += character.upper() 
        else:
            conversion_string += character
    return conversion_string

def solve(s):
    uppercase = 0
    lowercase = 0
    case = ''

    for character in s:
        if character.islower():
            lowercase += 1
        else:
            uppercase += 1

    if lowercase > uppercase or lowercase == uppercase:
        case = 'lower'
    else:
        case = 'upper'

    return lower_upper_convertion(case, s)

s = "CODe"

print(solve(s))