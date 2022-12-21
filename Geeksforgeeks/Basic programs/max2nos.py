#Given two numbers, write a Python code to find the Maximum of these two numbers.

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))


if(a > b):
    print("a is maximum")
else:
    print("b is maximum")

#==================================================
# 2nd way

def max(a,b):
    return (a > b)
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

if(max(a,b)):
    print("a is maximum")
else:
    print("b is maximum")

#===================================================
# 3rd way using ternary

def maximum(a,b):
    return (a > b)
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

print("a is maximum" if maximum (a,b) else "b is maximum")

#=================================================
#using max inbulit function
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

print("a is maximum" if max(a,b) else "b is maximum")
    