#WAP for Fibonacci series
num = int(input("Enter the number: "))
n1 = 0
n2 = 1
while n1 < num:
    print(n1, end = " ")
    n1, n2 = n2 , n1+n2