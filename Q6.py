# WAP to find compound interest: take P,T,R and n (how many times it compounds in a year) as input
p = int(input("Enter the principle: "))
t = int(input("Enter the time: "))
r = int(input("Enter the rate: "))
n = int(input("Enter the number: "))

ci = p*(1+(r/n))**(n*t)

print("The compound interest is: ", ci)