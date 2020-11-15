# Remove the parentheses
# In this kata you are given a string for example:

# "example(unwanted thing)example"
# Your task is to remove everything inside the parentheses as well as the parentheses themselves.

# The example above would return:

# "exampleexample"

# def remove_mode(str):
#     # remove
#     if character == ')':
#         remove_parentheses(s)

# def remove_mode(remove, s):


def remove_parentheses(s):
    corrected_str = ''

    number_of_open = 0
    number_of_close = 0

    remove = False
# remove mode
# print to new string mode

    for character in s:     
        
        if number_of_open > number_of_close:
            remove = True
        
        if character == '(':
            remove = True
            corrected_str += ''
            number_of_open += 1

        while remove:
            if character != ')':
                break
            else:
                remove = False
                number_of_close += 1

        if remove == True or character == ')':
            corrected_str += ''

        else:
            corrected_str += character


    # return remove == False

    return corrected_str

s = "hello example (words(more words) here) something"

print(remove_parentheses(s))