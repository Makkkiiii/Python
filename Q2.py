#WAP to take two numbers as input on a and b, display the actual value we get when we divide a by b, quotient and remainder. 
a = int(input('Enter the 1st number: '))
b = int(input("Enter the 2nd number: "))
print('The actual value we get when we divide a by b is: ', a/b)
print('The quotient is: ', a//b)
print('The remainder is: ', a%b)