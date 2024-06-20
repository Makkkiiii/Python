for i in range (1,6):
    print((str(i)*i))
print()

for i in range (1,6):
   print('*' *i)
print()

for i in range (5,0,-1):
    print('*' *i)
print()


for i in range (1,5):
     print(' ' * (4 - i) + '*' * i)
print()

for i in range (5, 0,-1):
    print(' ' * (5 - i) + '*' * i)
print()

ch = 'SUMAN'
for i in range(1,6):
    print(ch[:i])
print()

ch = 'SUMAN'
for i in range(5,0,-1):
    print(ch[:i])
print()

ch = 'SUMAN'
for i in range(1,6):
    print(ch[:i].rjust(5))
print()

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
