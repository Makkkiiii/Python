#WAP to display multiplication of a number in reverse order (i.e. 5*10=50 first and 5*1 =5 in last)

num = int(input("Enter the number: "))
for i in range(10,0,-1):
    print(num,"*",i,"=",num*i)
