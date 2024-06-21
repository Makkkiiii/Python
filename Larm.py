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


#FOR LOOP

# Armstrong or not
num = input("Enter the number: ")
sum = 0
for digit in num:
    sum += int(digit) ** 3
if sum == int(num):
    print("Armstrong")
else:
    print("Not Armstrong")
