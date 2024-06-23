ch = input("Enter a string: ")
count = 0
for i in ch:
    if i in "aeiou":
        count+=1
print("No. of vowel = ", count)


#While Loop

ch = input("Enter the string: ")

count = 0
index = 0 
while index < len(ch):
    if ch[index].lower() in 'aeiou':  
        count += 1
    index += 1  

print("The number of vowels are: ", count)
