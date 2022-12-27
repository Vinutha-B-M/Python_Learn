# Python – Words Frequency in String Shorthands

a = "hello i am vinutha, hi hello"
res = {key : a.count(key) for key in a.split()}
print(str(res))

#======================================
a = "hello i am vinutha, hi hello"
print({key : a.count(key) for key in a.split()})