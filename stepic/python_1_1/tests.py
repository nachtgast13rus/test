import math
from math import *
dicks = {}

def update_dictionary(dick, key, value):
    global dicks
    if key in dick:
        dick[key] += [value]
    else:
        key *= 2
        if key in dick:
            dick[key] += [value]
        else:
            dick[key] = [value]




update_dictionary(dicks, 1, -2)

print(math.pi)
