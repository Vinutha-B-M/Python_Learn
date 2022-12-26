#Python Program for Program to find area of a circle
#Area = pi * r2
#where r is radius of circle 

pi = 3.142
r = float(input("enter the radius :"))
area = pi * r * r
print(area)

#==========================================
pi = 3.142
r = float(input("enter the radius :"))
def area( pi, r):
    print("area", pi * r * r)
area(pi, r)

#==========================================
import math
def area():
    r = float(input("Enter radius : "))
    print(math.pi * pow(r,2))
area()

#===========================================
import math
r = float(input("Enter radius : "))
print(math.pi * pow(r,2))
