# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(string, ending):
    if string.endswith(ending):
        return True
    else:
        return False

print(solution('abc', 'bc'))

# CodeWars solution:
#     def solution(string, ending):
#         return string.endswith(ending)