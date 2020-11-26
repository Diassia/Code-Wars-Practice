# Python dictionaries are inherently unsorted. So what do you do if you need to sort the contents of a dictionary?

# Create a function that returns a sorted list of (key, value) tuples (Javascript: arrays of 2 items).

# The list must be sorted by the value and be sorted largest to smallest.

# Examples
# sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)]
# sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]

# def sort_dict(d):
#     sorted_list_tuples = []
#     sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
#     for i in sorted_dict:
#         sorted_list_tuples.append(tuple((i[0], i[1])))
#     return sorted_list_tuples
    
    # list(sorted_dict.items())

# def sort_dict(d):
#     sorted_dict = {k:d[k] for k in sorted(d)}
#     return list(sorted_dict.items())

def sort_dict(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

print(sort_dict({3:1, 2:2, 1:3}))
print(sort_dict({1:2, 2:4, 3:6}))
print(sort_dict({1:5, 3:10, 2:2, 6:3, 8:8}))


# CodeWars Solution:
    # def sort_dict(d):
    #   return sorted(d.items(), key=lambda x: x[1], reverse=True)