#Python program to check whether a number is Prime or not


num = 11
if (num > 1):
    for i in range(2, int(num/2) + 1):
        if (num % i )== 0: 
             print(num , "is not prime ")
             break
    else:
        print(num, "is prime")
else:
    print(num, "is not prime")

#=============================================
