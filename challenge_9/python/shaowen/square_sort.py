#!/home/shaowen/anaconda2/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 08:25:26 2017

@author: Shaowen Liu
"""

def square_sort(arr):
    """
    from [-2,-1,0,1,2] to [0,1,1,4,4]
    args:
        arr, list type
    """
    # retieve the negtive 
    a_list = [-i for i in arr if i < 0]
    # if arr has negtive numbers
    if a_list:
        b_list = arr[:len(a_list)-1:-1]
        # compare the elements and add into final list,O(n)
        res = []
        while a_list and b_list:
            if a_list[-1] <= b_list[-1]:
                res.append(a_list.pop(-1)**2)
            else:
                res.append(b_list.pop(-1)**2)
                
        # one of the list should be emtpy, clear the other one, O(n)
        return res + [o**2 for o in a_list[::-1] + b_list[::-1]]
    # if arr only has non-negtive numbers
    else:
        return [o**2 for o in arr]