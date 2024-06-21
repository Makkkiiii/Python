#1
for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("\n")
print()


#2
for i in range(5,0,-1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("\n")
print()

#3
for i in range(1,6):
    for j in range(5, i-1, -1):
        print(j, end=" ")
    print("\n")
print()

#4
for i in range(1, 6):
    for j in range(i, i + i):
        print(j, end=' ')
    print()


#OUTPUTS
'''
1 

1 2 

1 2 3 

1 2 3 4 

1 2 3 4 5


1 2 3 4 5

1 2 3 4

1 2 3

1 2

1


5 4 3 2 1

5 4 3 2

5 4 3

5 4

5


1
2 3
3 4 5
4 5 6 7
5 6 7 8 9

'''
