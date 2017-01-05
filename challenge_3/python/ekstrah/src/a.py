def findingMajoList(aList): #{
    bList = set(aList)
    bList = list(bList)
    for i in range(0, len(bList)): #{
        if aList.count(bList[i]) > len(bList): #{
            return bList[i]
        #}
    #}
#}



aList = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]

if __name__ == "__main__": #{
    val = findingMajoList(aList)
    print(val)
#}
