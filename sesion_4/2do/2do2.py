#
# generate a function to produce points 
# to be used as x-axis
# 
# INPUT
# -> a initial point
# -> b final point
# -> c increment
#
# OUTPUT
# <- list of points
#
# for instance for this range [1,10,.1]
# it will produce 100 points
# [1.0, 1.1, ... , 9.9, 10]
#
import matplotlib.pyplot as plt
import numpy as np

print("Ingresa punto inicial: ")
initial_p =  input()
print("Ingrsa punto final: ")
final_p = input()
print("Ingresa incremento: ")
increment = input() 

#Muestra el array 
list_p = np.arange(int(initial_p), int (final_p), float(increment))
print(list_p)
#imprime los puntos

plt.scatter (list_p, list_p )
plt.show()
