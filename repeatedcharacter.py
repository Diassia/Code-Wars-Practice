import collections

# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

# def letter_iterate(word):
#     for letter in word_string:
#         print(letter)

# def iterate_string(letter, word): # counter attempt
#     c = collections.Counter(word_string)
    
#     for letter in word_string:
#         c[word] += 1      

# #second function for "is x = y" with for loop

# def duplicate_encode(word):
#     duplicate_string = ''
#     for index, letter in enumerate(word_string [:-1]): #enumerate will loop over something (e.g. the string and count)
#         if letter == word_string[index+1]:
#             duplicate_string += ')'
#         else:
#             iterate_string(letter, word)
#             duplicate_string += '('
#     print(duplicate_string)

#     # iterate 'b' then iterate (to see if b matches), if b == b then print )

# # count()




# def number_of_letter_repetitions(letter, word):
    # for tracked_letter in word_string:
    #     count = 0
    #     if word_string.count(tracked_letter) > 1:
    #         count =+ 1
    #         if count > 1:
    #             return ')'
    #         else:
    #             return '('
             #this will keep returning )
    #for loop for iterating through letters and counting repetitions
        #if repetitions is > 1
            # count =+ 1
        #else ??? 

# def duplicate_encode(word):
    # new_string = ''
    # for letter in word_string:
    #     if letter == word_string: #index? - issue line
    #         new_string.join(')')
    #     else:
    #         number_of_letter_repetitions(letter, word)
    # print(new_string)
    # for loop to iterate through letters
        #if number_of_letter_repetitions > 1:
            #print ) to new string
        #else:
            #print ( to new string






























def duplicate_encode(word):
    result = ''
    # problem: map every letter in word to ( or ) based on whether or not more than 1 occurrence appears of that letter
    for letter in word:
        if number_of_times_letter_appears_in_word(letter, word) > 1:
            result += ')'
        else:
            result += '('
    return result

def number_of_times_letter_appears_in_word(letter_to_count, word):
    # problem: given a string 'a' and a string 'abcaef' 
    # find out how many times 'a' appears (in this case 2)

    count = 0
    for letter in word:
        if letter == letter_to_count:
            count += 1 
    return count


word_string = 'davina'
duplicate_encode(word_string)