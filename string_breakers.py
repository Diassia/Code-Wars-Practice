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
    string = st.replace(" ", "") # removes whitespace
    new_string = ''
    count = 0

    for i in range(len(string[count:])):
        chunk = string[count:count+n] # will take string in "n" chunks
        if count >= len(string):
            break
        else:
            new_string += chunk + '\n' # add new line break at the end of the chunk
            count += n

    return new_string[:-1] # remove the final new line break

print(string_breakers(5, 'This is an example string'))


# Top CodeWars solutions:
# from re import sub, findall

# def string_breakers(n, st):
#     return "\n".join(findall(".{" + str(n) + "}|.+", sub("\s", "", st)))

# OR

# def string_breakers(n, st): 
#     st = st.replace(' ', '')
#     return '\n'.join(st[i:i+n] for i in range(0, len(st), n))