#Python Program for factorial of a number

def fact(n):
    return 1 if(n == 1 or n == 0)else (n * fact(n - 1))
    
print(fact(5))

#=============================================
def factorial(n):
    if (n < 0):
        return 0
    elif(n == 0 or n == 1):
        return 1
    else:
        fact = 1
        while(n > 1):
            fact = fact * n
            n = n - 1
        return fact

num = 5  
print(factorial(num))      