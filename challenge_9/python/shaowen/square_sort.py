# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 08:25:26 2017

@author: Shaowen Liu
"""

def square_sort(arr):
    # retieve the negtive and non-negtive list,O(n)
    a_list = [-i for i in arr if i < 0]
    b_list = arr[len(a_list):][::-1]
    
    # compare the elements and add into final list,O(n)
    res = []
    while a_list and b_list:
        if a_list[-1] <= b_list[-1]:
            res.append(a_list.pop(-1)**2)
        else:
            res.append(b_list.pop(-1)**2)
            
    # one of the list should be emtpy, clear the other one, O(n)
    return res + [o**2 for o in a_list[::-1] + b_list[::-1]]