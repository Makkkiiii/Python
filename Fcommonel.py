def common_elements(lst1, lst2):
	return list(set(lst1) & set(lst2))

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
print(common_elements(lst1, lst2))

#Using Loop
def common_elements(lst1, lst2):
    common = []
    for i in lst1:
        if i in lst2 and i not in common:
            common.append(i)
    return common

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
print(common_elements(lst1, lst2))
