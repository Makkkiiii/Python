def find_max(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    max_x = find_max(lst[1:])
    return lst[0] if lst[0] > max_x else max_x

a = [3, 2, 1, 4, 5]
print(find_max(a))