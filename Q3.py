# WAP to calculate Surface area and volume of a cylinder, take user input
import math
pi = 3.14
r = int(input("Enter the radius: "))
h = int(input("Enter the height: "))

surface_area = 2*pi*r*(r+h)
volume = pi*r*r*h
print("The surface area is: ", surface_area)
print("The volume is: ", volume)