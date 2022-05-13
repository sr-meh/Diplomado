#
# select and write 
# one of the following stat functions
#
#from statistics import mode
import numpy as np
from scipy import stats

num_list = np.array([3, 5, 12, 34, 9, 7,3])

#def sum(lst): pass
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print("Sum (lst) function: ", sum((num_list)))


#def avg(l): pass
avg = sum(num_list)/len(num_list)
print("Avg function: ", round(avg,2))

#def min(l): pass
min_num = min(num_list)
print("Min function: ", min_num)

#def max(l): pass
max_num = max(num_list)
print("Max function: ", max_num)

#def range(l): pass
print ("Range (5): ", list(range(5)))

def std(l): pass


#def mode(l): pass
#mode_num_list = stats.mode(num_list)
#print("Mode function: ", mode_num_list[0][0])
print("Mode function: ",  (stats.mode(num_list)))