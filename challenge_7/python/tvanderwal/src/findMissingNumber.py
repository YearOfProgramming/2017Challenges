#Challenge 7: Return a missing integer from an unsort list of integers
"""
old solution. intList.sort() is O(nlogn) time and doesn't fit the challenge criteria
def findMissingNumber(intList):
    #sort list
    intList.sort()

    for i, val in enumerate(intList):
        if i != val:
            return i
"""

def findMissingNumber(intList):
    sumInts = sum(intList)
    sumRange = 0
    for i in range(1, len(intList) + 1):
        sumRange += i
    return sumRange - sumInts

if __name__ == '__main__':
    print(findMissingNumber([3, 2, 1]))