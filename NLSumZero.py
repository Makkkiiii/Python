sum = 0
while True:  
    n = 1  
    while n != 0: 
        n = float(input("Enter a number (0 to exit): "))
        if n == 0:
            break  
        sum += n
    break  

print(f"The sum is {sum}")
