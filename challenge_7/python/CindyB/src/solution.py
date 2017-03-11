def findMissing(values):
    result = sum(range(1,len(values)+1))
    for value in values:
        result -= value

    return result