from numpy import *
x=array([])
y=int(input("First Number:"))
z=int(input("Last Number:"))
for i in range(y,z):
    x=append(x,i)
    for i in range(5):
        x=append(x,0)
x=append(x,z)
print(x)