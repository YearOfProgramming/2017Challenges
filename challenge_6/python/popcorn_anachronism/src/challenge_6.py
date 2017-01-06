test1 = [1,2,3,4,8,9,10,12,13,14]
test2 = [1,2,3,4,9,10,15]

#store ranges as "min->max" in an array if they are not the same
def store_ranges(ranges, rangemin, rangemax):
    if rangemin != rangemax:
        ranges.append(str(rangemin) + "->" + str(rangemax))
    return ranges

#check for ranges (integers incrementing by 1) in an ordered array
def check_ranges(array):
    rangemin = array[0] #initialize the min and max to first entry
    rangemax = array[0]
    ranges = []         #store min-max range pairs

    #exit if array contains 0 or 1 element
    if len(array) < 2:
        return ranges

    #check if each element is incrementing by 1
    for i in range(1, len(array)):
        if array[i]-1 == array[i-1]:    #if so, increment rangemax
            rangemax = array[i]
        else:                           #if not, store the previous range and start with a new min
            store_ranges(ranges, rangemin, rangemax)
            rangemin = array[i]
    rangemax = array[i]                 #store last max
    store_ranges(ranges, rangemin, rangemax)
    return ranges

print(check_ranges(test1))
print(check_ranges(test2))

# Testing input with only 1 return value
assert check_ranges([1, 2]) == ["1->2"]

# Testing input with no return value
assert check_ranges([1]) == []

# Testing input with multiple return values
assert check_ranges([1,2,3,4,5,8,9,10]) == ["1->5", "8->10"]
