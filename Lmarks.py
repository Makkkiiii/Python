marks = [60,67,45,87,90,78,84,38,13,56]

# A
total = 0
count = 0
for i in marks:
    if i >= 60:
        count += 1
        total += i

# B
is_score_13 = 13 in marks

print("A. 60 or more: ", count)
print("A. Sum: ", total)
print("B. Who scored 13: ", is_score_13)

#WHILE LOOP

marks = [60,67,45,87,90,78,84,38,13,56]

total = 0
count = 0
index = 0
is_score_13 = False

while index < len(marks):
    mark = marks[index]
    if mark >= 60:
        count += 1
        total += mark
    if mark == 13:
        is_score_13 = True
    index += 1

print("A. 60 or more: ", count)
print("A. Sum: ", total)
print("B. Who scored 13: ", is_score_13)
