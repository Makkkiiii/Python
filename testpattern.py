num = 1
for i in range (1,5):
    for j in range(i):
        print(num, end = " ")
        num += 1
    print()
print()


'''
        1
      2 1
    3 2 1
  4 3 2 1 
5 4 3 2 1

'''
for i in range(1, 6):  
    for j in range(5 - i):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()