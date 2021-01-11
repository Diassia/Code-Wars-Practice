# I will give you an integer (N) and a string. Break the string up into as many substrings of N as you can without spaces. If there are leftover characters, include those as well.

# Example: 

# n = 5;

# st = "This is an example string";

# Return value:
# Thisi
# sanex
# ample
# strin
# g

# Return value as a string: 'Thisi'+'\n'+'sanex'+'\n'+'ample'+'\n'+'strin'+'\n'+'g'

def string_breakers(n, st):
    # remove spaces
    string = st.replace(" ", "")
    new_string = ''

    # split into n letter chunks and add new line
    # for i in range(len(string)):
    #     chunk = string[i:i+5]
    #     new_string += chunk + '\n'

    count = 0
    
    # while increment < len(string):
    for i in range(len(string[count:])):
        chunk = string[count:count+n]
        if count >= len(string):
            break
        else:
            new_string += chunk + '\n'
            count += n

    return new_string[:-1]

print(string_breakers(5, 'This is an example string'))