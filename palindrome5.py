#Write a Python program that determines whether a given string is a palindrome or not.

s = input("Enter a string: ")
s = s.replace(' ', '').lower()
if s == s[::-1]:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")