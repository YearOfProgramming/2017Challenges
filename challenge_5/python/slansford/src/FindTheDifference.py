#Imports Counter function from collections module
from collections import Counter

#Defines Solution class for test.py testing
class Solution(object):
	def findTheDifference(self, s, t):
		'''String 's' has one less letter than string 't',
		this function counts the occurence of each letter
		in each string and returns the character that does not have
		an equal occurence in string 's' when compared to string 't'.'''
		s_count = Counter(s)
		t_count = Counter(t)
		for char in t_count:
			if t_count[char] != s_count[char]:
				return char