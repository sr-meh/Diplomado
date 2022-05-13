#
# radious of circle inscribed in a tringle
# place here your solution code
#
# zeeAlso
# https://keisan.casio.com/exec/system/1223428152

import math 

print("INCIRCLE OF A TRIANGLE")

a = float (input('Ingresa la medida de lado A:'))
b = float(input('Ingresa la medida de lado B:'))
c = float (input('Ingresa la medida de lado C:'))

s = ((a+b+c)/2)

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

radius = area / s 
#Diameter
diameter = radius*2
#print ("radio: ", radius)
#r = (math.sqrt(s(s-a)(s-b)(s-c)/s))
#print (r)

# Incircle area
sc = (math.pi) * (radius**2)
#print (sc)

#Triangle area:
st = math.sqrt(s * (s-a)*(s-b)*(s-c))
#print ("St: ", st)
ratio =float (sc/st)

print ("radio: ", radius)
print ("diameter: ", diameter )
print ("incircle area Sc: ", sc )
print ("triangle area St: ",area )
print ("area ratio: ",ratio)