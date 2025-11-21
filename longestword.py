def longest_word(sentence):
    words = sentence.split()
    print(words)
    return max(words, key=len)

print(longest_word("The fox jumps over the lazy dog"))