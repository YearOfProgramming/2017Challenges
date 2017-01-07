def findMissingNumber(arr):
    wantedTotal = 0
    actualTotal = 0
    arrLen = len(arr)
    # Get the total of ALL the numbers (even the missing one)
    # Additionally, get the total of the ACTUAL list
    # Return the difference
    for i in xrange(arrLen+1):
        wantedTotal += i
        if i != arrLen:
            actualTotal += num[i]
    return wantedTotal - actualTotal

if __name__ == '__main__':
    print(findMissingNumber([1, 2, 3, 4, 0]))



# Things i do to work this out
# Total
#[0] [0,1] [0,1,2] [0,1,2,3] [0,1,2,3,4] [0,1,2,3,4,5]
#0      1       3       6       10          15
# Everytime a new number is added on the
# difference increments by one
# total = all numb added up
