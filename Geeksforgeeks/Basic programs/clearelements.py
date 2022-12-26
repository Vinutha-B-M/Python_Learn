#Different ways to clear a list in Python

list = [5,6,8,1,2,45]
list.clear()
print(list)

#====================================
list = [5,6,8,1,2,45]
list = []
print(list)

#====================================
list = [5,6,8,1,2,45]
del list[:]
print(list)

#====================================

list = [5,6,8,1,2,45]
while len(list) != 0:
    list.pop()
print(list)