ch = input("Enter a string: ")
count = 0
for i in ch:
    if i in "aeiou":
        count+=1
print("No. of vowel = ", count)


#While Loop

ch = input("Enter the string: ")

count = 0
i = 0 
while i < len(ch):
    if ch[i].lower() in 'aeiou':  
        count += 1
    i += 1  

print("The number of vowels are: ", count)
