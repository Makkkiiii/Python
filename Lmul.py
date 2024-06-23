#WAP to display multiplication of a number in reverse order (i.e. 5*10=50 first and 5*1 =5 in last)

num = int(input("Enter the number: "))
for i in range(10,0,-1):
    print(num,"*",i,"=",num*i)


#While loop

number = int(input("Enter the number: "))
i = 10

while i >= 1:
    result = number * i
    print(f"{number} * {i} = {result}")
    i -= 1
