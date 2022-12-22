#Python Program for compound interest
#A = P(1 + R/100) t 
#Compound Interest = A – P 
#A is amount 
#P is the principal amount 
#R is the rate and 
#T is the time span

p = int(input("Enter principal value : "))
t = int(input("Enter time value : "))
r = int(input("Enter rate value : "))

def compound_Interest(p,t,r):
    Amount = p * (pow((1 + r / 100), t))
    CI = Amount - p
    print("Compound interest is",CI)

compound_Interest(p,t,r)

