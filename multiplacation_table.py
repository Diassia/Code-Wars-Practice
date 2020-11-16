# Your task, is to create NxN multiplication table, of size provided in parameter.

# for example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]

def new_list(size, add_to_multiply, multiply_2):
    size_count = size
    new_table = []
    multiplication_no = multiply_2

    for number in range(size_count):
        multiply = add_to_multiply * multiplication_no # e.g. (size_count * multiply_2) (1*1), (1*2), (1*3)
        new_table.append(multiply)
        multiplication_no += 1

    return new_table

def multiplication_table(size):
    table = []
    multiply_2 = 1
    multiply_1 = 1
    size_count = size

    for number in range(size_count):
        multiply_2 + 1
        table_to_add = new_list(size, multiply_1, multiply_2)
        table.append(table_to_add)
        multiply_1 += 1
            
    return table

size = 10

print(multiplication_table(size))