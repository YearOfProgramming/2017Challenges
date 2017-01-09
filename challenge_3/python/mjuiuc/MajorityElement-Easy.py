from collections import Counter
from math import floor
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using 'Counter' from collections module reduces lines of code
        
        newTuple = Counter(nums).items()
        for i in newTuple:
            if i[1] > len(nums)/2:
                return i[0]
