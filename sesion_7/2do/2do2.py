#
# produce 10,000 coin flips
#
# print how many of them were:
# heads
# tails
#
import random
print ("Ingresa cuantas veces lanzas la moneda: ")
x = input()

def moneda():
    lanzamiento = [random.randint(1,2) for i in range(int (x))]
    sello = lanzamiento.count(1)
    aguila = lanzamiento.count(2)

    print("aguila: ", aguila, "sello: ", sello)

moneda()