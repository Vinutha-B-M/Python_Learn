#Python Program for How to check if a given number is Fibonacci number?
n = int(input("Enter fibonacci number :"))
def fib(n):
    if (n == 1):
        return 0
    elif (n == 2):
        return 1
    else:
        return (fib(n-1) + fib(n-2))
print(fib(n))