#
# select a distribution from numpy
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#
from numpy import random

random_num = random.rayleigh(scale=1.8, size=(2,3))
print (random_num)