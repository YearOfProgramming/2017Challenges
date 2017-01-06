
def ranges(arr):
        # Will store the final result
        ranges = []
        atStart = False
        sVal = 0 # Starting Value
        eVal = 0 # Ending Value
        # Loops through the array passed
        for i in xrange(len(arr)):
                if i != len(arr)-1: # If not at end
                        if not atStart: # Start of a new number?
                                atStart = True
                                sVal = arr[i] # Assigned sVal
                        if (arr[i] != (arr[i+1]-1)): # If the next number-1 is != to current then sequence is broken
                                atStart = False # To get a new start value
                                eVal = arr[i] # Last value has been found
                                if sVal != eVal: # Make sure its not just one number
                                        ranges.append('{0}->{1}'.format(sVal, eVal))
                else: # when at last 2nd val
                        eVal = arr[i] # Must be the end
                        if atStart: # Only append if was in a sequence
                                ranges.append('{0}->{1}'.format(sVal, eVal))
        return ranges

if __name__ == '__main__':
        val = ranges([1,3,4,5,7,8,9,14,15,16, 18, 19, 26,27,28, 30, 32,33,40])
        print val

# if not last number check first number with the next number
# if the next number is == to the second -1 then carry on else
# end number == arr[i]
        
