# Python Program to find largest element in an array

a = [5,10,15,20]
print(max(a))

#==================
arr = [10, 324, 45, 90, 9808]   
n = len(arr)
max = arr[0]
for i in range(1,n):
    if (arr[i] > max):
        max = arr[i]
print(max)
#======================

arr = [10, 324, 45, 90, 9808]   
arr.sort()
n = len(arr)
print(arr[n-1])
