def greet(lst):
    lst.sort(reverse = True)
    return lst

a = [3,1,2,4]
b = greet(a)
print(b)