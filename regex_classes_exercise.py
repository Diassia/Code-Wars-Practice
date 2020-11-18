import re

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a-leaping, 9 ladies dancing, 8 maids a-milking, 7 swans a-swimming, 6 geese a-laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics)) # return list


vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall(lyrics))

doubleVowelRegex = re.compile(r'[aeiou]{2}')
print(doubleVowelRegex.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping, 9 ladies dancing, 8 maids a-milking, 7 swans a-swimming, 6 geese a-laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'))

