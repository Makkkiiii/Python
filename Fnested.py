def flatten_list(nested_list):
    flattened_list = []
    for i in nested_list:
        for j in i :
            flattened_list.append(j)
    return flattened_list
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = flatten_list(a)
print(b)