# Remove the parentheses
# In this kata you are given a string for example:

# "example(unwanted thing)example"
# Your task is to remove everything inside the parentheses as well as the parentheses themselves.

# The example above would return:

# "exampleexample"

import re

def remove_parentheses(s):
    return re.sub(r'\(.*\)', '', s) # re.sub(pattern, repl, string, count=0, flags=0)

s = "a (bc d)e"

print(remove_parentheses(s))
