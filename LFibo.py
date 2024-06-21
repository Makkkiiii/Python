#WAP for Fibonacci series

#WHILE LOOP
num = int(input("Enter the number: "))
n1 = 0
n2 = 1
while n1 < num:
    print(n1, end = " ")
    n1, n2 = n2 , n1+n2



#FOR LOOP
num = int(input("Enter the number: "))
n1, n2 = 0, 1
for i in range(num):
    if n1 > num:
        break
    print(n1, end=" ")
    n1, n2 = n2, n1 + n2
