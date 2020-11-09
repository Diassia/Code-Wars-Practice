# This kata is about converting numbers to their binary or hexadecimal representation:

# If a number is even, convert it to binary.
# If a number is odd, convert it to hex.

def evens_and_odds(n):
    if (n % 2) == 0:
        return bin(n)[2:] # the slice removes the "0b" at the start
    else:
        return hex(n)[2:]

print(evens_and_odds(2))


    # CodeWars refactor code:
    # def evens_and_odds(n):
    #     return hex(n)[2:] if n % 2 else bin(n)[2:]