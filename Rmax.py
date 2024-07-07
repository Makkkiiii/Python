def find_max(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    max_x = find_max(lst[1:])
    return lst[0] if lst[0] > max_x else max_x

a = [3, 2, 1, 4, 5]
print(find_max(a))



#LOOP

def max_list(a,m,i):
    if i==len(a):
        return m
    else:
        if a[i]>m:
            m = a[i]
        return max_list(a,m,i+1)

a = [3,1,4,6,3]
m = max_list(a,a[0],0)
print("Largest  = ", m)
