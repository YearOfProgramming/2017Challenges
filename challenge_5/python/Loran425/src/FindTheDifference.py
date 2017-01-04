__author__ = "Loran425"
from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        # Old Implementation
        # count = {}
        # for char in s:
        #     if char not in count.keys():
        #         count[char] = 1
        #     else:
        #         count[char] += 1
        #
        # for char in t:
        #     if char not in count.keys():
        #         count[char] = -1
        #     else:
        #         count[char] -= 1
        s_count = Counter(s)
        t_count = Counter(t)
        s_count.subtract(t_count)

        for item in s_count.keys():
            if s_count[item] <= -1:
                return item

        return None
