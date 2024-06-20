marks = [60,67,45,87,90,78,84,38,13,56]

# A
a = [mark for mark in marks if mark >= 60]
b = len(a)
total = sum(a)

# B
is_score_13 = 13 in marks

print("A. 60 or more: ", b)
print("A. Sum: ", total)
print("B. Who scored 13: ", is_score_13)
