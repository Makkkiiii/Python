pi = 3.14
print("Which area do you want to print(1=Square, 2=Circle or 3=Rectangle)?")
choice = int(input("Enter the choice: "))

if choice == 1:
    l = int(input("Enter length: "))
    area = l*l
    print("Area = ",area)

elif choice == 2:
    r = int(input("Enter radius: "))
    area = pi * r * r
    print("Area = ",area)

else:
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    area = l * b
    print("Area = ",area)