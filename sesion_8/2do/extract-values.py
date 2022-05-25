#



#

import pandas as pd
csv = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')

# convert 1st variable as tuple
tupla = [(key, value) for key, value in csv.items()]

# convert 2nd variable as dictionary
diccionario = {key:value for key, value in csv.items()}

# convert 3rd variable as list
lista = [[key, value] for key, value in csv.items()]


print(tupla)
print(diccionario)
print(lista)