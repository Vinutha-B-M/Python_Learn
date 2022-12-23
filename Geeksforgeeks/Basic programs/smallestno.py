#Python program to find smallest number in a list
list = [20,90,45,12,56]
list.sort()
print("Enter smallest number in the list : ", list[0] )

#==============================================
list = [20,90,45,12,56]
print("Enter smallest number in the list : ", min(list) )

#================================================
#Python program to find smallest number in a list

from functools import reduce 
list = [20,90,45,12,56]
print("Enter smallest number in the list : ", reduce(min,list))