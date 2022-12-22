#Python program to swap two elements in a list


a = [23, 65, 19, 90]
def swap(a,first,last):
    temp = a[first]
    a[first] = a[last]
    a[last] = temp
    return a
    
    
first,last = 1,3
print(swap(a,first - 1,last- 1))    