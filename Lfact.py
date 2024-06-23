#WAP TO FIND THE FACTORIAL OF A NUMBER

num = int(input("Enter the number: "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print("The factorial of a number is: ",fact)

# While Loop

a = int(input("Enter the number: "))
i = 1
fact = 1
while i<=a:
    fact *= i
    i = i + 1
print('The fact is = ', fact)
