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

#WHILE LOOPS

#1. 
i = 1
while i < 6:
    print(str(i) * i)
    i += 1

#2
i = 1
while i < 6:
    print('*' *i)
    i += 1

#3
i = 5
while i > 0:
    print('*' *i)
    i -= 1

#4
i = 1
while i < 5:
    print(' ' * (4 - i) + '*' * i)
    i += 1

#5
i = 5
while i > 0:
    print(' ' * (5 - i) + '*' * i)
    i -= 1

#6
ch = 'SUMAN'
i = 1
while i <= len(ch):
    print(ch[:i])
    i = i + 1   

#7 
ch = 'SUMAN'
i = 5
while i > 0:
    print(ch[:i])
    i -= 1

#8 
ch = 'SUMAN'
i = 1
while i <= len(ch):
    print(ch[:i].rjust(5))
    i += 1

#9
ch = 'SUMAN'
i = len(ch)
while i > 0:
    print(ch[:i].rjust(5))
    i -= 1


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
