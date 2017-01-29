# Ranges

def ranges(int_list):
    """
    Given a sorted list of integers function will return
    an array of strings that represent the ranges
    """
    begin = 0
    end = 0

    ranges = []

    for i in int_list:
        # At the start of iteration set the value of
        # `begin` and `end` to equal the first element
        if begin == 0:
            begin = i
            end = i
        # Set the current element as the value of `end`
        # as long as the array is in sequence
        elif i-1 == end:
            end = i
        # Reset flags to current element when iterating through
        # multiple integers that are of broken sequence
        elif begin == end:
            begin = i
            end = i
        else:
        # Sequence of array has been broken, append current range
        # to `ranges` and set the value of `begin and `end` flags to
        # equal the current element
            ranges.append("{0}->{1}".format(begin, end))
            begin = i
            end = i
    # Grab the last range from the array
    if begin != end:
        ranges.append("{0}->{1}".format(begin, end))

    return ranges


if __name__ == "__main__":
        # Test your own implementation
        # Input the size of the array
        # Then enter each integer value
        size = int(input())
        ints = [int(input()) for _ in range(size)]
        print(ranges(ints))
