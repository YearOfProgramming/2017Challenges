# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 08:14:08 2017

@author: Shaowen Liu
"""

"""
find the missing number from arr, compared with an integral list.
args:
    arr, a list with a missed number
"""
findMissing = lambda arr: set(range(len(arr)+1)).difference(set(arr)).pop()
