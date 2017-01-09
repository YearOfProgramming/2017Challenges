# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 09:24:29 2017

@author: Shaowen liu
"""
def ranges(arr):
    """
    para arr, a python list    
    """
    if not arr: return []
    res = []
    # set inital cursor start and end
    start = end = arr[0]
    for i in arr[1:]:
        # if arr in seuquence, update end
        if i == end + 1:
            end = i
        # if arr diverged, reset start & end
        else:
            if start != end:
                res.append('%s->%s'% (start, end))
            start = end = i
    # complete the last range
    if start != end:
        res.append('%s->%s'% (start, end))
    return res

#arr = [1,2,3,4,5,8,9,10]
#print ranges(arr)


