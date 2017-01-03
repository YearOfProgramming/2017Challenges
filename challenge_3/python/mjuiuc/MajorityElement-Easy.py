from collections import defaultdict
from math import floor
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # I knew how to do this instantly! YAY :) granted it was easy, I can
        # now see that there's progress. When I started this I probably would've
        # struggled to come up with a solution to this problem, but with practice
        # I knew exactly what method to use to solve this quickly.
        n = len(nums)
        histo = defaultdict(int)
        for i in nums:
            histo[i] += 1
        for key in histo:
            if histo[key] > floor(n/2):
                return key