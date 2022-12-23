#Reversing a List in Python

list = [1,2,3,4,5,6]
list.reverse()
print(list)

#=======================================
list = [1,2,3,4,5,6]
emptylist = []
for i in list:
    emptylist.insert(0, i)
print(emptylist)

#=======================================
list = [1,2,3,4,5,6]
new_list = list[::-1]
print(new_list)