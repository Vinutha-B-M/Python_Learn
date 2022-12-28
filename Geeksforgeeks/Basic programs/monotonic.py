# Python Program to check if given array is Monotonic

a = [9,8,7,6]
x = []
y = []
x.extend(a)
y.extend(a)
x.sort()
y.sort(reverse=True)
print("is monotonic" if (x == a or y == a) else "is not monotonic" )
