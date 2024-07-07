def string_rev(s1, i):
    a = len(s1)
    if i == 0:
        return ""
    else:
        return s1[i-1]+string_rev(s1, i-1)
    
name = 'jhilke'
rev_name = string_rev(name, len(name))
print(f"Reverse of {name} is {rev_name}")