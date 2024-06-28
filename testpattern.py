num = 1
for i in range (1,5):
    for j in range(i):
        print(num, end = " ")
        num += 1
    print()
print()


'''
1 
2 3 
4 5 6 
7 8 9 10 
'''


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

#WHILE LOOP
i = 1
while i < 6:
    j = 0
    while j < (5 - i):
        print(" ", end=" ")
        j += 1
    
    k = i
    while k > 0:
        print(k, end=" ")
        k -= 1
    
    print()
    i += 1
