def find_max(num1, num2, num3):
    
    return max(num1, num2, num3)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

maximum = find_max(num1, num2, num3)
print(f"The maximum number is: {maximum}")