#Write a Python program that finds the maximum of three numbers. (without nested if-else)
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))
if num1 > num2 and num1 > num3:
    print("Maximum is", num1)
elif num2 > num1 and num2 > num3:
    print("Maximum is", num2)
else:
    print("Maximum is", num3)