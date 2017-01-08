from collections import Counter

class Solution:
    def findTheDifference(self, s, t):
        s_counter = Counter(s)
        t_counter = Counter(t)
        for letter in t_counter:
            if t_counter[letter] != s_counter[letter]:
                return letter

solution = Solution()
print(solution.findTheDifference('abc', 'abcd'))
