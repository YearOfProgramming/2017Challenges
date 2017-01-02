from collections import defaultdict
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Lazy solution here... exceeds runtime of course
        # for i in nums:
        #     if nums.count(i) == 1:
        #         return i
        
        #Do this without using extra memory? That's too hard. K well this worked and beat 50% cases so :/
        #Basically took a histogram of the list and then go back through it to find the number whose count
        #was one
        histo = defaultdict(int)
        for num in nums:
            histo[num] += 1
        for num in nums:
            if histo[num] == 1:
                return num