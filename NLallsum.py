n = int(input("Enter a number: "))

while n > 9:
    sum = 0
    for digit in str(n):
        sum += int(digit)
    n = sum

print("Single digit number: ", n)