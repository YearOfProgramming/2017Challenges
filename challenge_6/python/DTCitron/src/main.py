def rangefinder(t):
    # List of ranges
    ranges = []
    if len(t) < 2:
        return ranges

    # Start at the very beginning
    rangestart = t[0]
    rangeend = t[0]

    for i in range(1,len(t)):
        # Check if the next entry is in the same range as the current range start
        if rangeend+1 == t[i]:
            rangeend = t[i]
        else:
            # If not, check that the range has length > 0 -> 
            if rangeend > rangestart:
                ranges.append(str(rangestart) + '->' + str(rangeend))
                rangestart = t[i]
                rangeend = t[i]
            else:
            # Ignore ranges of length 0
                rangestart = t[i]
                rangeend = t[i]
    if rangeend > rangestart:
        ranges.append(str(rangestart) + '->' + str(rangeend))
    return ranges


if __name__=="__main__":
    t1 = [1,2,3,4,8,9,10,12,13,14]
    t2 = [1,2,3,4,9,10,15]
    t3 = [1,2]
    t4 = [1]
    t5 = [1, 2, 3, 14, 25, 30, 31, 32]
    t6 = [5,6,9,10,12,13,15,16,18,19,25,30]
    print 'Input: ', t1
    print 'Output: ', rangefinder(t1)
    print 'Input: ', t2
    print 'Output: ', rangefinder(t2)
    print 'Input: ', t3
    print 'Output: ', rangefinder(t3)
    print 'Input: ', t4
    print 'Output: ', rangefinder(t4)
    print 'Input: ', t5
    print 'Output: ', rangefinder(t5)
    print 'Input: ', t6
    print 'Output: ', rangefinder(t6)