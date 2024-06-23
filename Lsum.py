#WAP to find sum of n natural number

num = int(input("Enter the number: "))
sum = 0
for i in range(1,num+1):
    sum = sum + i
    print("The sum of n natural number is: ",sum)


# While Loop
a = int(input("Enter the number: "))
i = 1
sum = 0
while i<=a:
    sum += i
    i = i + 1
print('The sum is = ', sum)
