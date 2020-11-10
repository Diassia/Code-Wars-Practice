# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

def areYouPlayingBanjo(name):
    if name.startswith('R') or name.startswith('r'):
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'

name = 'Kayleigh'
print(areYouPlayingBanjo(name))

name = 'Richard'
print(areYouPlayingBanjo(name))

name = 'richard'
print(areYouPlayingBanjo(name))

    # CodeWars Solution:
    # def areYouPlayingBanjo(name):
    #     if name[0].lower() == 'r':
    #         return name + ' plays banjo'
    #     else:
    #         return name + ' does not play banjo'