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
