from collections import Counter


class Solution:
    def findTheDifference(self, s, t):

        s = dict(Counter(s))
        t = dict(Counter(t))

        for key in t.keys():
            if key not in s.keys():
                s[key] = 0
            if s[key] - t[key] <= -1:
                return key


if __name__ == '__main__':

	test_case = Solution()
	s, t = [input() for _ in range(2)]
	print('\n' + test_case.findTheDifference(s, t))