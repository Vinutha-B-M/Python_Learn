# Python Program for simple interest

p = 10
t = 20
r = 15
simple_interest  = (p*t*r)/100
print(simple_interest)

#=============================================
p = int(input("Enter principle value : "))
t = int(input("Enter time value : "))
r = int(input("Enter rate value : "))

def simple_Interest(p,t,r):
    return (p*t*r)/100
    
print(simple_Interest(p,t,r))