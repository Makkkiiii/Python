#Write a Python program that determines the season (spring, summer, autumn, or winter) based on a given month.
month = input("Enter the month: ")

spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']

if month in spring:
    print("Spring")
elif month in summer:
    print("Summer")
elif month in autumn:
    print("Autumn")
elif month in winter:
    print("Winter")
else:
    print("Invalid month")