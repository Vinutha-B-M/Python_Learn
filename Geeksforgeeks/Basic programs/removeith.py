#Ways to remove i’th character from string in Python

a = "welcome"
b = ''
pos = 5
for i in range(len(a)):
    if i != pos:
        b = b + a[i]
print(b)

#===================================
a = input("Enter a word : ")
b = ''
pos = int(input("Enter position : "))
for i in range(len(a)):
    if i != pos:
        b = b + a[i]
print(b)

#===================================
a = input("Enter a word : ")
pos = int(input("Enter position : "))
b = ''
b = a[:pos] + a[pos+1:]
print(b)