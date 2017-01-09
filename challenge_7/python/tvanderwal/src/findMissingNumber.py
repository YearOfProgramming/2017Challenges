#Challenge 7: Return a missing integer from an unsort list of integers

def findMissingNumber(intList):
    #sort list
    intList.sort()

    for i, val in enumerate(intList):
        if i != val:
            return i

if __name__ == '__main__':
    print(findMissingNumber([3, 2, 1]))