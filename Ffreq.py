def display_char_frequency():
    string = input("Enter a string: ")
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    for char, count in frequency.items():
        print(f"'{char}': {count}")

display_char_frequency()