from collections import Counter

class Solution(object):
	def findTheDifference(self, s, t):
		s_count = Counter(s)
		t_count = Counter(t)
		for char in t_count:
			if t_count[char] != s_count[char]:
				return char