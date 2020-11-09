# Messi is a soccer player with goals in three leagues:

# LaLiga
# Copa del Rey
# Champions
# Complete the function to return his total number of goals in all three leagues.

# Note: the input will always be valid.

# For example:

# 5, 10, 2  -->  17

# original code:
#     def goals(laLiga, copaDelRey, championsLeague):
#     pass

def goals(laLiga, copaDelRey, championsLeague):
    goals_total = laLiga + championsLeague + copaDelRey
    return goals_total

laLiga = 43
championsLeague = 10
copaDelRey = 5

print(goals(laLiga, copaDelRey, championsLeague))