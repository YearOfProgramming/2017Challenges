# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 09:20:09 2017
@author: shaowen Liu
"""

class Solution():
    def findTheDifference(self,s,t):
        if s==t: return None
        # combine s and t into st, and sorted
        st = sorted(s+t)
        stack = []
        for o in st:
            # filter out the one not in pairs
            if stack == []:
                stack.append(o)
            elif stack[-1] == o:
                stack.pop()
            elif stack[-1] != o:
                return stack[-1]
        # return the target if it's the last one
        return stack[-1]