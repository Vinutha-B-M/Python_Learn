#Python Program for cube sum of first n natural numbers

num = int(input("Enter a number : "))
sum = 0
for i in range(1, num + 1):
    sum = sum + pow(i, 3)
print(sum)
