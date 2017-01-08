# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 10:39:39 2017

@author: shaowen Liu
"""

def single_n(alist):
    n_dict = dict()
    for i in alist:
        n_dict[i] = n_dict.get(i,0) + 1
    return [k for k, v in n_dict.items() if v == 1]
