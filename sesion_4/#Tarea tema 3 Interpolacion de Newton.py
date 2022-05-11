#Tarea tema 3 Interpolacion de Newton
# 1. Dados: (-4, -2) y (1, 5) estimar el valor para x cuando y+ 3.7
# 2. Dados: (-2, 4), (-1, -2), (3,5) y (4.3, 11) estimar el valor de y, cuando x+ 7.7
# 3. Dados: (-1, 3), (0, -7), (4, 7) y (5, 11) estimar el polinomio interpolante  


import math

#3
#b1 = (y1-y0) / (x1-x0)
b1 = (-7-3)/(0-(-1))
print (b1)

#b2 = (y2-y1/x2-x1) - (b1) / (x2-x0)
b2 = ((7 -(-7) )/(4-0) - (b1)) / (4-(-1))
print (b2)

#b3 = ((y3-y2) / (x3-x2) - (y2-y1) / (x2-x1)) / (x3-x1) - b2
b3 = (((11-7)/(5-4) - (7-(-7))/(4-0)) / (5-0)) - (b2) / (5-(-1))
print (b3)