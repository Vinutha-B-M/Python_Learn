#Python program to interchange first and last elements in a list
#find 1st element of the list & store in var
#find last element of the list & store in var
#delete 1st & last element frm the list
#add last var value in first element of the list
#add first var value in last element of the list

a = ['apple','banana','orange','cherry']
first = a[0]
last = a[len(a)- 1]
a.pop(0)
a.pop(len(a)- 1)
a.insert(0, last)
a.insert(len(a) ,first)
print(a)

#=========================================

a = ['apple','banana','orange','cherry']
def swap(a,first,last):
    temp = a[first]
    a[first] = a[last]
    a[last] = temp
    return a
print(swap(a,0,len(a)- 1))    