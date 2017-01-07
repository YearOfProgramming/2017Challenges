def findMajorityElement(myArray):
    for x in myArray:
        count = sum(map(lambda s: s == x,myArray))
        if count > len(myArray)//2:
            return x
array = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7] 
print findMajorityElement(array)
