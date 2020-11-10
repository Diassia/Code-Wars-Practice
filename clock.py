# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

# Your task is to make 'Past' function which returns time converted to milliseconds.

# Example:
# past(0, 1, 1) == 61000

# Input constraints: 0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59

# def past(h, m, s):
#     convert_hours = h * 3600000
#     convert_minutes = m * 60000
#     convert_seconds = s * 1000
#     return convert_hours + convert_minutes + convert_seconds

def past(h, m, s):
    return (h * 3600000) + (m * 60000) + (s * 1000)

h = 0
m = 1
s = 1

print(past(h, m, s))

    # CodeWars solution:
    #     def past(h, m, s):
    #         return (3600*h + 60*m + s) * 1000