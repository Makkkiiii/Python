# WAP to find the roots of a quadratic equation: ax2+bx+c=0
import cmath 

a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b:  '))
c = float(input('Enter the value of c: '))

dis = (b**2) - (4*a*c)

s1 = (-b-cmath.sqrt(dis))/(2*a)
s2 = (-b+cmath.sqrt(dis))/(2*a)

print('The roots are: ', s1, s2)