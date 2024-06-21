names = ['nispal', 'tilak', 'bharat', 'rijesh', 'soniya']
vowels = 'aeiouAEIOU'

for name in names:
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    print(f"{name} contains {count} vowels")