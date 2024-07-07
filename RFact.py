def recursion(n):
    if n==0 or n==1:
        return 1
    else:
        return n*recursion(n-1)

num = int(input("Enter the number: "))
fact = recursion(num)
print("Total sum = ", fact)