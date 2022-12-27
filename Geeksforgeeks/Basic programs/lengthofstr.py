# Find length of a string in python (6 ways)

a = "vinutha"
print(len(a))

#========================
a = "vinutha"
count = 0
for i in a:
    count = count + 1
print(count)

#========================
a = "vinutha"
count = 0
while a[count : ]:
    count = count + 1
print(count)

#========================
a = "Hello"
b = "welcome" 
c= "vinu"

def vinuthaMethod(a): 
  count = 0   
  while a[count:]: 
    count += 1 
  print(count) 
 
vinuthaMethod(a)
vinuthaMethod(b)
vinuthaMethod(c)


