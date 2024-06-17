num = int(input("Enter a decimal number: "))
choice = input("Enter the conversion (binary, octal, hexadecimal): ")

if choice == "binary":
    print(bin(num))
elif choice == "octal":
    print(oct(num))
elif choice == "hexadecimal":
    print(hex(num))
else:
    print("Invalid")