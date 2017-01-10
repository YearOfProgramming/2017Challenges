def rangefinder(t):
    # List of ranges
    ranges = []

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
    print rangefinder(t1)
    print rangefinder(t2)
    print rangefinder(t3)
    print rangefinder(t4)
    print rangefinder(t5)
    print rangefinder(t6)