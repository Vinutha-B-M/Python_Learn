# Python program to find the sum of all items in a dictionary

dict = {'a': 100, 'b': 200, 'c': 300}
def returnSum(myDict):
	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)

	return final
print("Sum :", returnSum(dict))

#=================================
myDict = {'a': 100, 'b': 200, 'c': 300} 
list = [] 
for i in myDict: 
    list.append(myDict[i]) 
print("sum is ",sum(list))

#=========================
myDict = {'a': 100, 'b': 200, 'c': 300} 
sum = 0
for i in myDict.values(): 
    sum = sum + i
print(sum)
