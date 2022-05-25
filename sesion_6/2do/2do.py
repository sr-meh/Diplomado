#
# please refer to PPT file
# for exercise
#
from math import sin, sqrt

def fn(x):
    return 2*(sin(sqrt(x))-x)

a=0
b=1.9724
r1=fn(a)*(b-a)
print("Regla del rectangulo: ", r1)

pmedio= (a+b)/2
r2= fn(pmedio)*(b-a)
print("Regla de punto medio: ", pmedio)

def fn1(y):
    return (pow(7,-y))+3

c=-1
d=2
r3= ((d-c)/2)*(fn1(c)+fn1(d))
print("Regla del trapecio: ", r3)

n= (c+d)/2
r4=((d-c)/6)*(fn1(c)+4*fn1(n)+fn1(d))
print("Regla de Simpson:", r4)