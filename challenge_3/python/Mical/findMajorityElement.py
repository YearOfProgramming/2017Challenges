# Mical | 02/01/2017

from math import *

def findElement(things):
    maj = floor((len(things)/2))
    for element in list:
        c = things.count(element)
        if c >= maj:
            print(element)
            break
        else:
            continue

things = [2,2,3,4,5,6,7,5,4,3,2,4,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
findElement(things)

# I amplified the amount of 7's because the amount in the example wasn't enough to actually make it the majority element