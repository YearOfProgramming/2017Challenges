from collections import Counter


class Solution:
    def findTheDifference(self, s, t):

        s = Counter(s)
        t = Counter(t)

        for key in t.keys():
            if s[key] != t[key]:
                return key



if __name__ == '__main__':

	test_case = Solution()
	s, t = [input() for _ in range(2)]
	print('\n' + test_case.findTheDifference(s, t))