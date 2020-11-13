# In this Kata, you will write a function doubles that will remove double string characters that are adjacent to each other.

# For example:

# doubles('abbcccdddda') = 'aca', because, from left to right:

# a) There is only one 'a' on the left hand side, so it stays.
# b) The 2 b's disappear because we are removing double characters that are adjacent. 
# c) Of the 3 c's, we remove two. We are only removing doubles. 
# d) The 4 d's all disappear, because we first remove the first double, and again we remove the second double.
# e) There is only one 'a' at the end, so it stays.
# Two more examples: doubles('abbbzz') = 'ab' and doubles('abba') = "". In the second example, when we remove the b's in 'abba', the double a that results is then removed.

# The strings will contain lowercase letters only. More examples in the test cases.


def doubles(s):
    new_string = s
    test_letter1 = ''
    test_letter2 = ''
    for character in s:
        if character + character = True:

        
        
        # current_chara = character
        # adjacent_chara = len(s) - (current_chara + 1)
        # if current_chara == adjacent_chara:
        #     new_string.replace(character, '')
        # else:
        #     new_string += character
        # if s[index] == s[index+1]: #this is out of range
        #     new_string.replace(s[index], '')
        #     new_string.replace(s[index + 1], '')

print(doubles('abbbzz'))