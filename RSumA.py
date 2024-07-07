def sum_of_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_of_list(lst[1:])

a = [3, 2, 1, 4, 5]
print(sum_of_list(a))