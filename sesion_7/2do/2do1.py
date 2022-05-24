#
# first homework of the day
#

#lst= ['4','3','2','1',]
#brujula =['norte','sur','este','oeste',]

#print ("NUMERO RANDOM:",random.choice(brujula))

import random

puntos_cardinales =['norte','sur','este','oeste']
print ("Cuantos pasos quieres dar: ")
x =input()
print(random.choices(puntos_cardinales, k = int (x)))
