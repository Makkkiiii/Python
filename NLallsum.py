n = int(input("Enter a number: "))

while n > 9:
    sum = 0
    for i in str(n):
        sum += int(i)
    n = sum

print("Single digit number: ", n)
