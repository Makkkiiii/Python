def recursion(n):
    if n==0:
        return 0
    else:
        return n+recursion(n-1)

num = int(input("Enter the number: "))
sum = recursion(num)
print("Total sum = ", sum)