# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

def letter_iterate(word):
    for letter in word_string:
        print(letter)

#second function for "is x = y" with for loop

def duplicate_encode(word):
    duplicate_string = ''
    for index, letter in enumerate(word_string [:-1]): #enumerate will loop over something (e.g. the string and count)
        if letter == word_string[index+1]:
            duplicate_string += ')'
        else:
            duplicate_string += '('
    print(duplicate_string)

    # iterate 'b' then iterate (to see if b matches), if b == b then print )

# count()

word_string = 'kayleigh!'

letter_iterate(word_string)
duplicate_encode(word_string)
