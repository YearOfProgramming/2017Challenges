from collections import defaultdict


def findMajorityElement(lst):
    """
    lst: list of entries to find a majority element from
    return: majority element

    "Majority element" here refers to an element of a list that occurs the "majority" of the time (i.e. more than
    half of the elements are identical to the majority element).

    If no majority element is found, the function returns None.
    """
    dd = defaultdict(int)
    n = len(lst)
    for i in lst:
        dd[i] += 1
    for key in dd:
        if dd[key] > n // 2:
            return key
    return None

#  print(findMajorityElement([2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]))
#  outputs: 7