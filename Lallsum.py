# WAP to find the sum of all the digits of a number enter by the user

num = int(input("Enter the number: "))
sum = 0
while num > 0:
    sum = sum + num % 10
    num = num // 10
print("Sum of all = ", sum)
