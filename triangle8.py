#Write a Python program that determines the type of a triangle based on the given side lengths.(equilateral, isosceles , scalene) without nested if-else
a = int(input("Enter the sides of the triangle: "))
b = int(input("Enter the sides of the triangle: "))
c = int(input("Enter the sides of the triangle: "))

if a == b == c:
    print("Equilateral triangle")
elif a != b and b != c and a != c:
    print("Scalene triangle")
else:
    print("Isosceles triangle")