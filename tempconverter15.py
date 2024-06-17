
choice = int(input('Enter your choice: 1 for C to F and 2 for F to C: '))
temperature = float(input("Enter the temperature you want to convert: "))
if choice == 1:
    print ("The temperature in Fahrenheit is: ", (temperature * 9/5) + 32)
elif choice == 2:
    print ("The temperature in Celsius is: ", (temperature - 32) * 5/9)