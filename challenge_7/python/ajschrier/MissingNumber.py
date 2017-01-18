def builtInMethod(inputList):
    for i in xrange(len(inputList)):
        if i not in inputList:
            return i
    return 0


def sumMethod(inputList):
    fullSum = (len(inputList) * (len(inputList) + 1)) / 2
    return fullSum - sum(inputList)


def main():
    pass


if __name__ == '__main__':
    main()
