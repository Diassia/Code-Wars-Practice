# Remove the parentheses
# In this kata you are given a string for example:

# "example(unwanted thing)example"
# Your task is to remove everything inside the parentheses as well as the parentheses themselves.

# The example above would return:

# "exampleexample"

def remove_parentheses(s):
    corrected_str = ''

    number_of_open = 0
    number_of_close = 0

    remove = False

    for character in s:     
        if character == '(':
            remove = True
            number_of_open += 1
        elif character == ')':
            number_of_close += 1
            if number_of_open > number_of_close:
                remove = True
            else:
                remove = False
        elif remove == False:
            corrected_str += character

    return corrected_str

s = "hello example (words(more words) here) something"

print(remove_parentheses(s))