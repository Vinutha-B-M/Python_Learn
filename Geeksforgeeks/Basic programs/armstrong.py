#Python Program to check Armstrong Number

num = 153
numlist = (list(str(num)))
sum = 0
for i in numlist:
   sum = sum + pow(int(i) , len(numlist))
   
print("yes, is armstrong" if sum == num else "not armstrong")