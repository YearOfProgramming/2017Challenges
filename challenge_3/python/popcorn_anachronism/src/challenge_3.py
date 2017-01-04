a = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]

def majority_element(array):
    n = len(array)
    array_freq = {}     #dict of frequencies of items in array
    for item in array:
        if item in array_freq:  #if item already present in dict, increment by 1
            array_freq[item] = array_freq[item] + 1
        else:                   #otherwise add item to dict with frequency of 1
            array_freq[item] = 1
    for item in array_freq:     #check for item with majority frequency
        if array_freq[item] >= int(n/2):
            return item         
    return("No majority found. :(") #if not present, error message

print(majority_element(a))

