#
# select a distribution from random
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#

#random.triangular(low, high, mode)
import random

#limite inferior
low = 1
#limite superior
high =5
#sesgo
mode =3

for i in range(5):
    #imprime un numero aleatorio entre low y high, acercandose hacia el rangod de sesgo
    print(random.triangular(low, high, mode))