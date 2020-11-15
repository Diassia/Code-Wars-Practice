# Your task is to create a function called sum_arrays(), which takes two arrays consisting of integers, and returns the sum of those two arrays.

# The twist is that (for example) [3,2,9] does not equal 3 + 2 + 9, it would equal '3' + '2' + '9' converted to an integer for this kata, meaning it would equal 329. The output should be an array of the the sum in a similar fashion to the input (for example, if the sum is 341, you would return [3,4,1]). Examples are given below of what two arrays should return.

# [3,2,9],[1,2] --> [3,4,1]
# [4,7,3],[1,2,3] --> [5,9,6]
# [1],[5,7,6] --> [5,7,7]
# If both arrays are empty, return an empty array.

# In some cases, there will be an array containing a negative number as the first index in the array. In this case treat the whole number as a negative number. See below:

# [3,2,6,6],[-7,2,2,8] --> [-3,9,6,2] # 3266 + (-7228) = -3962

def convert_list_to_int(array):
    array_str_list = [str(integer) for integer in array]  # list comprehension to convert int into str
    single_string = ''.join(array_str_list) # .join string
    if single_string == '': # to prevent value error on ''
        single_string = 0
    return int(single_string) # convert back to int for future sum

def sum_arrays(array1, array2):
    if array1 == [] and array2 == []:
        return []

    sum_int = convert_list_to_int(array1)
    sum_int += convert_list_to_int(array2)

    sum_list = [int(x) for x in str(sum_int) if x != '-'] # List comprehension to convert integer into a list and ignore '-'
    
    if sum_int < 0: # converts the first number to negative if the first number was negative in sum_int
        sum_list[0] *= -1 

    return sum_list

array1 = [-9, 5, 7, 1]
array2 = []

print(sum_arrays(array1, array2))