str1 = "ram123@baha23dur#"
str2 = ""
str3 = ""

for char in str1:
    if char.isalpha():
        str2 += char
    elif char.isdigit():
        str3 += char

print("Alphabets:", str2)
print("Numbers:", str3)