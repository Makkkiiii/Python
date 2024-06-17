#Write a Python program that checks if a given number is divisible by  5 and 7 using 
#nested if-else statements. display message like :"divisible by both", "divisible by 5 but not with 7" and so on.
num = int(input("Enter a number: "))

if num % 5 == 0:
    if num % 7 == 0:
        print("Divisible by both 5 and 7")
    else:
        if num % 5 == 0:
            if num % 7 != 0:
                print("Divisible by 5 but not by 7")
            else:
                if num % 5 != 0:
                    if num % 7 == 0:
                        print("Divisible by 7 but not by 5")
                    else:
                        print("Not divisible by 5 and 7")