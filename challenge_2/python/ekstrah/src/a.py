def findingSingleList(aList): #{
    bList = list(set(aList))
    for item in bList: #{
        if aList.count(item) == 1: #{
            return item
        #}
    #}
#}




if __name__ == "__main__": #{
    aList = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
    val = findingSingleList(aList)
    print(val)
#}
