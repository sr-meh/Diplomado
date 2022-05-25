#
# please refer to PPT file
# for exercise
#

#e^(2-x)-7x=0
from math import exp


def fn():
    i= 0
    for repeticion in range(4):
        resultado=newton(i)
        print ("Resultado", {resultado})
        x=resultado
    return i

def newton(x):
    x1=exp(2-x)-7*x
    x2=-exp(2-x)-7
    return x-x1/x2

print("Resultado: ",{fn()})