# Main program for challenge 2 

from array_maker import *

# get a random array
set = getArray()

# make a repository to store values until their pair is found
storageBin = []

for elem in set:
    if not elem in storageBin:
        storageBin.append(elem)
    else:
        storageBin.remove(elem)
        
print('The odd man out is %d\n' %storageBin[0])
