def return_longest_word():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

print(return_longest_word())
