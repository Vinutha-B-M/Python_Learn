#Python program to find sum of elements in list

list = [1,2,3,4,5,8,9]
sum = 0
for i in list:
    sum = sum + i
print(sum)

#==============================

list = [1,2,3,4,5,8,9]
sum = 0
i = 0
while (i < len(list)):
    sum = sum + list[i]
    i = i + 1
print(sum)

#===============================
list = [1,2,3,4,5,8,9]
print(sum(list))

#===============================
from operator import*
list = [1,2,3,4,5,8,9]
result = 0
for i in list:
    result = add(i,result)
print(result)

