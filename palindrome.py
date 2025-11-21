import sys

str = input("Enter a string : ")

print(str)

print(str[::-1])

if str==str[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")