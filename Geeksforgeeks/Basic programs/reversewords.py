#Reverse words in a given String in Python

a = "welcome"
b = a[::-1]
print("is palindrome" if a == b else "not palindrome")

#===============================================
a = "welcome"
b = ''.join(reversed(a))
print(b)