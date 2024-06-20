#WAP to find sum of n natural number

num = int(input("Enter the number: "))
sum = 0
for i in range(1,num+1):
    sum = sum + i
    print("The sum of n natural number is: ",sum)