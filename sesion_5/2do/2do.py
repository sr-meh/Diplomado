#
# please refer to PPT file
# for exercise
#
#si f(x)=sen^3*2x/x^4+1 obtener f´(2.45)


from scipy.misc import derivative
from math import sin, exp



""" def fn(x):
    return x-exp(2*x)+4

def ck(a,b):
    n=fn(b)*a - fn(a)*b
    d=fn(b)- fn(a)
    return n/d

#c1
a=.5
b=1
print(ck(a,b))

#c2
a=.5
b=1
print(ck(a,b)) """

def fn(x):
    return (sin(2 * x) ** 3) / (x ** 4 + 1)

#le aplica derivada a la funcion 
print(derivative(fn, 2.45)) 

