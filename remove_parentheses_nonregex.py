# Remove the parentheses
# In this kata you are given a string for example:

# "example(unwanted thing)example"
# Your task is to remove everything inside the parentheses as well as the parentheses themselves.

# The example above would return:

# "exampleexample"

def remove_parentheses(s):
    corrected_str = ''

    bracket_depth = 0

    for character in s:     
        if character == '(':
            bracket_depth += 1
        elif character == ')':
            bracket_depth -= 1
        elif bracket_depth == 0:
            corrected_str += character

    return corrected_str

s = "hello example (words(more words) here) something"

print(remove_parentheses(s))