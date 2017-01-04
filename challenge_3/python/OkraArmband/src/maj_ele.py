from collections import defaultdict


def findMajorityElement(lst):
    dd = defaultdict(int)
    n = len(lst)
    for i in lst:
        dd[i] += 1
    for key in dd:
        if dd[key] > n // 2:
            return key
    return None
