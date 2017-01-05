def nonRepeatFinder(aList) : #{
    bList = set(aList)
    bList = list(bList)
    cList = []
    for i in range(0, len(bList)): #{
        if(aList.count(bList[i])) == 1:
            cList.append(bList[i])
    return cList
    #}
#}

if __name__ == "__main__" : #{

    aList = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7,11]
    print(nonRepeatFinder(aList))
#}
