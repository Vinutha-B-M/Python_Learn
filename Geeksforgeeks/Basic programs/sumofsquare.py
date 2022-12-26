#Python Program for Sum of squares of first n natural numbers

num = int(input("Enter a number : "))
sum = 0
for i in range(1, num):
    sum = sum + pow(i, 2)
print(sum)