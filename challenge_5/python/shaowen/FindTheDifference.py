# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 09:20:09 2017
@author: shaowen Liu
"""

class Solution():
    def findTheDifference(self,s,t):
        """
        para 1: s, string type
        para 2: t, string type
        """
        # combine s and t into st, and sort it
        st = sorted(s+t)
        cursor = None
        for o in st:
            # filter out the one not in pairs
            if cursor == None:
                cursor = o
            elif cursor == o:
                cursor = None
            else:
                return cursor
        # if the target happends to be the last one
        return cursor