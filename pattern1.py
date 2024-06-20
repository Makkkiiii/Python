#1
for i in range (1,6):
    print((str(i)*i))
print()

#2
for i in range (1,6):
   print('*' *i)
print()

#3
for i in range (5,0,-1):
    print('*' *i)
print()

#4
for i in range (1,5):
     print(' ' * (4 - i) + '*' * i)
print()

#5
for i in range (5, 0,-1):
    print(' ' * (5 - i) + '*' * i)
print()

#6
ch = 'SUMAN'
for i in range(1,6):
    print(ch[:i])
print()

#7
ch = 'SUMAN'
for i in range(5,0,-1):
    print(ch[:i])
print()

#8
ch = 'SUMAN'
for i in range(1,6):
    print(ch[:i].rjust(5))
print()

#9
ch = 'SUMAN'
for i in range(5, 0, -1):
    print(ch[:i].rjust(5))

'''
1
22
333
4444
55555

*
**
***
****
*****

*****
****
***
**
*

   *
  **
 ***
****

*****
 ****
  ***
   **
    *

S
SU
SUM
SUMA
SUMAN

SUMAN
SUMA
SUM
SU
S

    S
   SU
  SUM
 SUMA
SUMAN

SUMAN
 SUMA
  SUM
   SU
    S
'''
