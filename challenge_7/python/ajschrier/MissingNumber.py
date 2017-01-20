def builtInMethod(inputList):
    for i in xrange(len(inputList)):
        # Check if i is in list
        if i not in inputList:
            # Return number
            return i
    # Return 0 if none of the numbers meet the condition
    return 0


def sumMethod(inputList):
    # find (n*n+1)/2
    fullSum = (len(inputList) * (len(inputList) + 1)) / 2
    # subtract sum of full range from supplied range
    return fullSum - sum(inputList)


def main():
    pass


if __name__ == '__main__':
    main()
