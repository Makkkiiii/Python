marks = [60,67,45,87,90,78,84,38,13,56]

# A
a = []
total = 0
for mark in marks:
    if mark >= 60:
        a.append(mark)
        total += mark
b = len(a)

# B
is_score_13 = False
for mark in marks:
    if mark == 13:
        is_score_13 = True
        break

print("A. 60 or more: ", b)
print("A. Sum: ", total)
print("B. Who scored 13: ", is_score_13)
