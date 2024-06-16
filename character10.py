#Write a Python program that checks if a given character is an alphabet, digit, or special character.
char1 = input("Enter the character: ")
if char1.isalpha():
    print("The character is an alphabet")
elif char1.isdigit():
    print("The character is a digit")
else:
    print("Special character")