def invert(list):
    list_negative = [-x for x in list]
    return list_negative

list = [1,2,3,4,5]

print(invert(list))