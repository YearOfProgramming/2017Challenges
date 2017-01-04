__author__ = "Loran425"


class Solution(object):
    def findTheDifference(self, s, t):
        count = {}
        for char in s:
            try:
                count[char] += 1
            except LookupError:
                count[char] = 1
                
        for char in t:
            try:
                count[char] -= 1
            except LookupError:
                count[char] = -1
                
        for item in count.keys():
            if count[item] <= -1:
                return item

        return None
