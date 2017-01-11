def square(aList):
    return map(lambda x: x**2, aList)

def merge(listOne, listTwo):
    result = []
    while listOne and listTwo: #while both the lists still have elements
        if listOne[0] < listTwo[0]:
            result.append(listOne.pop(0)) #pops the first element from listOne from listOne and adds it to result
        else: #listOne[0] == listTwo[0] or listTwo[0] < listOne[0]
            result.append(listTwo.pop(0))
    #now one of the lists is empty and we can just add all the remaining contents of the nonempty list into result
    if listOne:
        result += listOne #concatenating lists is done with plus operator
    if listTwo:
        result += listTwo

    return result

def get_break_index(aList):
    index = 0 #this will be the index at which we break the list in two
    for i in range(len(aList)):
        if aList[i] > 0: #it's a positive number!
            index = i #this is where the first positive number in the list is
            break #we break here so that index remains the first positive number in the list
    return index

def challenge9(aList):
    break_index = get_break_index(aList)

    listOne = aList[0:break_index] #we know this will be the negative half
    listTwo = aList[break_index:]

    a = square(listOne)[::-1] #we need to reverse this since [-3,-2,-1] --> square --> [9,4,1]
    b = square(listTwo)

    return merge(a,b)


# a = [-3,-2,0,3,4,6]
# print challenge9(a)
