def findingMajoList(aList, default=None): #{
    count = 0
    candi = default

    for num in aList: #{
        if count != 0: #{
            count += 1 if candi == num else -1
        #}
        else:
            candi = num
            count = 1
    #}
    return candi if aList.count(candi) > len(aList) // 2 else default ###Checking Again
#}



if __name__ == "__main__": #{
    aList = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]
    val = findingMajoList(aList)
    print(val)
#}
