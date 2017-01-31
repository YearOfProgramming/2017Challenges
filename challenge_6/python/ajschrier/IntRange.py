ARROW = '->'


def outputRange(inputList):
    # Helper Vars
    outputList = []
    rangeStart = None
    rangeEnd = None

    for i in inputList:
        # Detect the beginning of the list
        if rangeStart is None:
            rangeStart = i
            rangeEnd = i
        # Check for invalid sequence
        elif rangeEnd is not i-1:
            # If vars are equal, no sequence is being terminated
            if rangeStart is rangeEnd:
                rangeStart, rangeEnd = i, i
            # If they're not, add the terminated sequence to the list
            # and continue
            else:
                outputList.append('{}{}{}'.format(rangeStart, ARROW, rangeEnd))
                rangeStart, rangeEnd = i, i
        # If none of the above, continue the current sequence
        else:
            rangeEnd = i

    # Check to see if a sequence is in progress at the end of the loop
    if rangeStart is not rangeEnd:
                outputList.append('{}{}{}'.format(rangeStart, ARROW, rangeEnd))
    return outputList


def main():
    print outputRange([1, 2, 3, 4, 8, 9, 10, 12, 13, 14])
    print outputRange([1, 2, 3, 4, 5, 8, 9, 10])


if __name__ == '__main__':
    main()
