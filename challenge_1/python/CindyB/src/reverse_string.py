import sys

def reverseString(myInput):
    if not myInput:
        return None
    
    returnValue = ""
    for letter in myInput:
        returnValue = letter + returnValue
        
    return returnValue

if len(sys.argv) >= 2:
    print reverseString(sys.argv[1])
