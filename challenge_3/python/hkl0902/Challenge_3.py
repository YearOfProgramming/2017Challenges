import math
from collections import Counter
lst = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]

c = Counter(lst)
n = len(lst)

def findMajorityElement():
    for key, val in c.items():
        if val >= math.floor(n/2):
            return key
