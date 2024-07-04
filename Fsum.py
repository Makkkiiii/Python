def sum_sq(num):
    total = 0  
    for i in range(1, num+1):
        total += i*i  
        
    return total

num = int(input("Enter a number: "))
totalsum = sum_sq(num)
print(f"Sum of sq numbers till {num} is {totalsum}")