# WAP to find the sum of all the digits of a number enter by the user

#WHILE LOOP
num = int(input("Enter the number: "))
sum = 0
while num > 0:
    sum = sum + num % 10
    num = num // 10
print("Sum of all = ", sum)


#FOR LOOP
num = int(input("Enter the number: "))
sum = 0
for i in str(num):
    sum += int(i)
print("Sum of all = ", sum)
