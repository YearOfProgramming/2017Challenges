from sets import *
import sys

def unrepeat(input):
    # Set that holds all unique elements in the input
    holder = set()
    # Set that holds all repeated elements in the input
    repeats = set()

    # Loop through input once, checking for repeating elements
    for i in input:
        if i not in holder:
            holder.update({i})
        else:
            repeats.update({i})
    # The non-repeated element will be the difference between holder and repeats
    # If there was one non-repeated element, return it
    try:
        print(list(holder-repeats)[0])
    except:
        print("No non-repeated elements")


if __name__=="__main__":

    # These are the two lists where we will be returning the element that is not repeated 
    input = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
    input2 = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]
    # An extra check: a case with zero non-repeated elements
    input3 = [1,2,1,2,3,3,4,4] 

    unrepeat(input)
    unrepeat(input2)
    unrepeat(input3)
