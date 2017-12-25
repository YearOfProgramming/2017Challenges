class Solution:
	def findTheDifference(self, s, t):
		v = list(s)

		for c in t:
			if c not in v:
				return(c)

		return(None)