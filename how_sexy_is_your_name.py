# How sexy is your name? Write a program that calculates how sexy one's name is according to the criteria below.

# There is a preloaded dictionary of letter scores called SCORES(python) / $SCORES (ruby). Add up the letters (case-insensitive) in your name to get your sexy score. Ignore other characters.

# The program must return how sexy one's name is according to the "Sexy score ranking" chart.

#        score <= 60:   'NOT TOO SEXY'
#  61 <= score <= 300:  'PRETTY SEXY'
# 301 <= score <= 599:  'VERY SEXY'
#        score >= 600:  'THE ULTIMATE SEXIEST'

scores = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
            'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
            'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
            'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}

def sexy_name(name):
    sexy_calculation = 0

    for letter in name:
        if letter == ' ':
            continue
        sexy_calculation += scores.get(letter.upper(), 0)

    if sexy_calculation <= 60:
        return 'NOT TOO SEXY'
    elif 61 <= sexy_calculation <= 300:
        return 'PRETTY SEXY'
    elif 301 <= sexy_calculation <= 599:
        return 'VERY SEXY'
    elif sexy_calculation >= 600:
        return 'THE ULTIMATE SEXIEST'

print(sexy_name('GUV'))
print(sexy_name('BOB'))
print(sexy_name('ROBBY'))
print(sexy_name('CodeWars'))
print(sexy_name('Kayleigh'))
print(sexy_name('Stephen Shaw'))



# key_list = list(scores.keys())
# val_list = list(scores.values())

    # for letter in name:
    #     if letter == ' ':
    #         continue
    #     position = key_list.index(letter.upper()) #identifies whether the number is in the values list
    #     sexy_calculation += val_list[position]