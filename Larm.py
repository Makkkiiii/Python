# Armstrong or not

#WHILE LOOP
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
num = input("Enter the number: ")
sum = 0
for i in num:
    sum += int(i) ** 3
if sum == int(num):
    print("Armstrong")
else:
    print("Not Armstrong")
