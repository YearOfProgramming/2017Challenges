from collections import Counter

class Solution:
    def findTheDifference(self, s, t):
        s = Counter(s)
        t = Counter(t)

        for i in t:
            if s[i] == 0 or t[i] != s[i]:
                return i

