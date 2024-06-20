ch = input("Enter a string: ")
count = 0
for i in ch:
    if i in "aeiou":
        count+=1
print("No. of vowel = ", count)