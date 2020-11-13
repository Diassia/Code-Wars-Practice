# Complete the solution so that it reverses all of the words within the string passed in.

# Example:

# reverseWords("The greatest victory is that which requires no battle")
# // should return "battle no requires which that is victory greatest The"

def reverseWords(s):
    reverseString = s.split() #split the words into a list: ['hello', 'world!']
    reverseString.reverse() #reverse the list: ['world!', 'hello']
    return " ".join(reverseString) # join back into string: 'world! hello'

s = "hello world!"

print(reverseWords(s))


    # CodeWars Solution:
    # def reverseWords(str):
    #     return " ".join(str.split(" ")[::-1])