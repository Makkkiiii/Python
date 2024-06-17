#Write a Python program that checks if a given year is a leap year or not, using nested if-else statements.
year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 != 0:
        print("Leap year")
    else:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")