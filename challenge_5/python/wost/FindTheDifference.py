class Solution(object):
    def findTheDifference(self, s, t):
        s, t = list(s), list(t)
        return list(set(t)-set(s))[0] if set(t)-set(s) != set() else None
