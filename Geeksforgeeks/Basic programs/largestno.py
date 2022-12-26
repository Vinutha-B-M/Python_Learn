#Python program to find largest number in a list

from functools import reduce 
list = [20,90,45,12,56]
print("largest number in the list : ", reduce(max,list))

#=================================================
list = [20,90,45,12,56]
print(max(list))
#=================================================
list = [20,90,45,12,56]
print("largest number in the list :" , max(list))

