def repeat_string(num_string, position): # maybe include reverse option for flipped rules
    converted_string = ''
    number_position = position
    lowercase = True
    string_to_repeat = num_string # string

    while number_position > len(converted_string):
        if lowercase == True:
            converted_string += num_string
            lowercase = False
        else:
            converted_string += (string_to_repeat).upper()
            lowercase = True
    
    sliced_string = converted_string[:position]

    return sliced_string

print(repeat_string('four', 10))