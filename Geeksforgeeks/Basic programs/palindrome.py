# Python program to check if a string is palindrome or not

a = "malan"
def Palindrome(a):
    return a[::-1]
if a == Palindrome(a):
    print("is palindrome")
else:
    print("is not palindrome")

#=============================
a = "gadag"
def Palindrome(a):
    b = ''.join(reversed(a))
    return b
if a == Palindrome(a):
    print("is palindrome")
else:
    print("is not palindrome")

#====================================
a = "hello"
b = ""
for i in a:
    b = i + b
if (a == b):
    print("Yes")
else:
    print("No")

#===========================

a = "welcome"
b = a[::-1]
print("is palindrome" if a == b else "not palindrome")