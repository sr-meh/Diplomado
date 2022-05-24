#
# please refer to PPT file
# for exercise
#

import math

# 1. Dados: (-4, -2) y (1, 5) estimar el valor para x cuando y+ 3.7
x0 = -4
x1 = 1
y= 3.7
y0 = -2
y1 = 5

i_lineal = (((x1 - x0) / (y1-y0)) * (y-y0) + x0) 
print ("E1 Iterpolacion lineal: "),(i_lineal)

# 2. Dados: (-2, 4), (-1, -2), (3,5) y (4.3, 11) estimar el valor de y, cuando x+ 7.7 Interpolacion de Newton

#b1 = ((y1)-(y0)) / ((x1)-(x0))
b1 = (-2-4)/(-1-(-2))
#print (b1)

#b2 = (y2-y1/x2-x1) - (b1) / (x2-x0)
b2 = ((5 -(-2) )/(3-(-1)) - (b1)) / (3-(-2))
#print (b2)

#b3 = ((y3-y2) / (x3-x2) - (y2-y1) / (x2-x1)) / (x3-x1) - b2 / x3 -x0
b3 = ((((11-5)/(4.3-3) - (5-(-2))/(3-(-1))) / (4.3-(-1))) - (b2)) / (4.3-(-2))
#print (b3)

#y = y0 + b1(x - x0) + b2(x - x0)(x - x1) + b3(x - x0)(x - x1)(x - x2)
b4 = (4 + (b1*(7.7-(-2)))) + ((b2*(7.7-(-2))*(7.7-(-1)))) + ((b3*(7.7-(-2))*(7.7-(-1))*(7.7-3)))
print ("E2 Interpolcacion de Newton: ", (b4)) 


# 3. Dados: (-1, 3), (0, -7), (4, 7) y (5, 11) estimar el polinomio interpolante  

#y = (((x-x1)*(x-x2)*(x-x3)/(x0-x1)*(x0-x2)*(x0-x3))*(y0) +)
#y = ((((x-3.2)*(x-4))/((x-2)*(x-3.2)))*1.43) + ((((x-2)*(x-4))/(3.2-2)*(3.2-4))*2.79) + ((((x-2)*(x-3.2))/(4-2)*(4-3.2))*3.56)
#print (y)

#https://www.youtube.com/watch?v=ItD69ydUrs8