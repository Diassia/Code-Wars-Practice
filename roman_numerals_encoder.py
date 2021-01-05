# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

# Example:

# solution(1000) # should return 'M'

numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

key_list = list(numerals.keys())
val_list = list(numerals.values())

# def convert_number(number_to_convert): #this should be a single number
#     converted_numerals = ''
#     previous_numerals = ''
#     number = number_to_convert


    # return converted_numerals


def roman_numerals_calculation(number):
    number_to_convert = number
    roman_numerals = ''

    contains_number = number_to_convert in numerals.values() #works for simple numbers in dict
    if contains_number == True:
        position = val_list.index(number_to_convert) #identifies whether the number is in the values list
        return key_list[position] #returns the position of the key that corresponds to the number
    else:
        for value in val_list:
            if number_to_convert % value:
                position = val_list.index(number_to_convert)
                roman_numerals += key_list[position]

        
        # if len(str(number_to_convert)) == 1:
        #     if number_to_convert % 5 == 0:
        #         roman_numerals += 'V'
        #     else:
        #         roman_numerals += ('I' * number_to_convert)
        # elif len(str(number_to_convert)) == 2:
        #     if str(number_to_convert[0]) == 1:
        #         roman_numerals += 'X'
        #     elif str(number_to_convert[0]) == 5:
        #         roman_numerals += 'L'
        #     elif number_to_convert % 50 == 1:
        #         remaining_number = number_to_convert - 50
        #         if remaining_number % 10 == 1:
        #             second_remaining_number = remaining_number - 10
            
        #     if number_to_convert % 10 == 0:
        #         roman_numerals += 'X'
        #     roman_numerals = ''
        # elif len(str(number_to_convert)) == 3:
        #     roman_numerals = ''
        # elif len(str(number_to_convert)) == 4:
        #     roman_numerals = ''
        
    return roman_numerals

    # for number in number_to_convert:
    #     # roman_numerals += convert_number(number_to_convert)

    #     # if previous_numerals[-1] == 'I':
    #     #     number - 1

    # return roman_numerals

print(roman_numerals_calculation(1))
print(roman_numerals_calculation(3))
print(roman_numerals_calculation(5))
print(roman_numerals_calculation(21))
print(roman_numerals_calculation(1000))
print(roman_numerals_calculation(1889))