# Python program to print even length words in a string

str1 = "Hello I am Vinutha"
for each in str1.split():  
    print(each if(len(each)%2== 0) else "")

#======================================
str1 = "Hello I am Vinutha"
b = str1.split()
print(b)
for each in str1.split():
    if len(each)%2== 0:
        print(each)