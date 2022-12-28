# Python Program for array rotation
#1) Reverse the entire list by swapping first and last numbers
   #i.e start=0, end=size-1
#2) Partition the first subarray and reverse the first subarray, by swapping first and last numbers.
 #  i.e start=0, end=size-d-1
#3) Partition the second subarray and reverse the second subarray, by swapping first and last numbers.
 #  i.e start=size-d, end=size-1

def reverse(start,end,arr):

	no_of_reverse = end-start+1
	count=0
	while((no_of_reverse)//2!=count):
		arr[start+count],arr[end-count] = arr[end-count],arr[start+count]
		count+=1
	return arr

def left_rotate_array(arr,size,d):

	start=0
	end=size-1
	arr=reverse(start,end,arr)
	
	start=0
	end=size-d-1
	arr=reverse(start,end,arr)
	
	start=size-d
	end=size-1
	arr=reverse(start,end,arr)
	return arr
	
arr=[1,2,3,4,5,6,7,8]
size=8
d = int(input("Enter no of rotation in list :"))
print('Original array:',arr)
print(left_rotate_array(arr,size,d))

