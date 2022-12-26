#Check if element exists in list in Python

list = [1, 2, 3, 4, 5, 6]
value = int(input("Enter any value : "))
if value in list:
    print("Yes ")
else:
    print("No")
#print("yes" if value in list else "no")
#=====================================
list = [1, 2, 3, 4, 5, 6]
value = int(input("Enter any value : "))
print("exist" if list.count(value) else "not exist") 