#write a Python program to find the addition of these two numbers

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
sum = a + b
print(sum)

#===========================================
#second way

def add(x,y):
    return x + y

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("addition of two numbers is : " ,add(a,b))    
