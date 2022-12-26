#Python | Check if a Substring is Present in a Given String

a = "I am vinutha"
print("yes" if 'am' in a else "no")

#================================
a = input("Enter a string : ")
b = input("Enter a substring : ")
print("yes" if b in a else "no")

#==================================
a = input("Enter a string : ")
b = input("Enter a substring : ")
if a.find(b) == -1:
    print("is not substring")
else:
    print("is substring")

#=================================
a = input("Enter a string : ")
b = input("Enter a substring : ")
if a.count(b) > 0:
    print("is substring")
else:
    print("is not substring")
