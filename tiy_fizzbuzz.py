# In this exercise, you will have to create a function named tiyFizzBuzz. This function will take on a string parameter and will return that string with some characters replaced, depending on the value:

# If a letter is a upper case consonants, replace that character with "Iron".
# If a letter is a lower case consonants or a non-alpha character, do nothing to that character
# If a letter is a upper case vowel, replace that character with "Iron Yard".
# If a letter is a lower case vowel, replace that character with "Yard".

def is_vowel(char):
    all_vowels = 'aeiouAEIOU'
    return char in all_vowels

def tiy_fizz_buzz(string):
    new_string = ''
    for character in string:
        if character.isupper():
            if is_vowel(character) == True:
                new_string += 'Iron Yard'
            else:
                new_string += 'Iron'
        elif character.islower():
            if is_vowel(character) == True:
                new_string += "Yard"
            else:
                new_string += character
        else:
            new_string += character
    return new_string  

print(tiy_fizz_buzz("A"))

    # CodeWars solution:
    # def tiy_fizz_buzz(s):
    #     return "".join(("Iron "*c.isupper() + "Yard"*(c.lower() in "aeiou")).strip() or c for c in s)