# generate random arrays for challenge_2 in python
from random import *

# Seed RNG
seed()

# Generate a 51 element random array. Each array is
# built with 21 pairs of values then shuffled.
# We'll stick to elements under 100 just for simplicity
def getArray():
    array = []
    for i in range(25):
        elem = randint(1, 100)
        array.append(elem)
        array.append(elem)
        
    array.append(randint(1, 100))
    
    shuffled = []
    
    while len(array) > 1:
        i = randint(0, len(array) - 1)
        shuffled.append(array.pop(i))
    shuffled.append(array[0])
    return shuffled
