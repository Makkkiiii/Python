# Armstrong or not
num = int(input("Enter the number: "))
sum = 0
a = num
while num > 0:
    sum = sum + (num % 10) ** 3
    num = num // 10
if sum == a:
    print("Armstrong")
else:
    print("Not Armstrong")