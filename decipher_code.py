# You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

# For each word:

# the second and the last letter is switched (e.g. Hello becomes Holle)
# the first letter is replaced by its character code (e.g. H becomes 72)
# Note: there are no special characters used, only letters and spaces

# Examples

# decipherThis('72olle 103doo 100ya'); // 'Hello good day'
# decipherThis('82yade 115te 103o'); // 'Ready set go'

import re

def decipher_word(word):
    decodeRegex = re.compile(r'(?P<digits>[\d]+)(?P<letters>\w*)')
    m = re.match(decodeRegex, word)
    no_match = m.group('digits')
    letter_match = m.group('letters')
    word_decipher = chr(int(no_match)) + letter_match

    # second and last letter are switched:
    word_list = list(word_decipher)
    if len(word_decipher) > 1:
        word_list[1], word_list[-1] = word_list[-1], word_list[1]
        word_decipher = ''.join(word_list)

    return word_decipher

def decipher_this(string):
    word_string = string.split()
    deciphered_string = ' '.join([decipher_word(word) for word in word_string]) # list comprehension

    return deciphered_string

print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))
print(decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"))
print(decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"))
print(decipher_this("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"))
print(decipher_this("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"))