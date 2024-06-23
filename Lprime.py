num = int(input("Enter the number: "))
count = 0

for i in range (1, num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")


#While Loop

num  = int(input("Enter the number: "))
count = 0 
i = 1
while i <= num:
    if num % 1 == 0:
        count += 1
        i += 1
if count == 2:
        print ("Prime")
else:
        print("Not Prime")
