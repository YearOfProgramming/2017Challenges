import time
from collections import Counter

#easy test case. solution = 7
a = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]

#more challenging test case. solution = 3
#a = [1,2,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,41,2,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,33,3,3,3,3,3,3,3,3,3,4,5,5,6,6,7,7,7,8,8,8,8,8,2,2,3,4,4,5,5,5,5,5,5,5,5,5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,6,7,7,7,6,5,5,4,3,23,2,2,3,3,3,4,4,4,3,3,4,4,5,65,6,6,5,5,4,3,2,2,3,3,34,3,3,4,4,3,3,3,3,3,3,3,988,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,33,3,3,3,3,3,3,3,3,3,4,5,5,6,6,7,7,7,8,8,8,8,8,2,2,3,4,4,5,5,5,5,5,5,5,5,5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,6,7,7,7,6,5,5,4,3,23,2,2,3,3,3,4,4,4,3,3,4,4,5,65,6,6,5,5,4,3,2,2,3,3,34,3,3,4,4,3,3,3,3,3,3,3,988]
#a=a*10000

#old version using dicts
def majority_element_old(array):
    n = len(array)
    array_freq = {}     #dict of frequencies of items in array
    for item in array:
        if item in array_freq:  #if item already present in dict, increment by 1
            array_freq[item] = array_freq[item] + 1
        else:                   #otherwise add item to dict with frequency of 1
            array_freq[item] = 1
    for item in array_freq:     #check for item with majority frequency
        if array_freq[item] > int(n/2):
            return item         
    return "No majority found. :(" #if not present, error message

#new version using counter
def majority_element(array):
    n=len(array)
    a_count = Counter(array)
    for item in a_count:
        if a_count[item] > int(n/2):
            return item
    return "No majority found. :("

start = time.clock()
print(majority_element_old(a))
print("time_oldversion: %.3f seconds" % (time.clock()-start))

start = time.clock()
print(majority_element(a))
print("time_newversion: %.3f seconds" % (time.clock()-start))

