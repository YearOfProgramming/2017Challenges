
def rangeFinder(inputList):
    '''finds the range of consecutive elements in an int-only list,
    and appends the range to an output list in the format "x->y"'''

    #ensures list isn't empty
    if inputList == None or len(inputList) == 1:
        return []

    outputList = list()
    start = inputList[0]
    end = 0
    newList = list()

    '''iterates through the range of the length of the input list
    and appends consecutive ranges to the output list'''
    for i in range(1,len(inputList)):
        if inputList[i] != (inputList[i-1] + 1):
            end = inputList[i-1]
            outputList.append("{}->{}".format(start, end))
            start = inputList[i]

        if i == len(inputList) - 1:
            end = inputList[i]
            outputList.append("{}->{}".format(start, end))

    #returns the output list built with ranges from input list
    return outputList