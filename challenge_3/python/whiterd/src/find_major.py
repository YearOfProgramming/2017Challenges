#!/usr/bin/env python

'''
    Input:  An array of integers.

    Output:  The single integer that occurs most often.
'''

from __future__ import print_function
from collections import Counter

given_array = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]

def find_major(array):
    counted = Counter(array)
    return counted.most_common(1)[0][0]


print(find_major(given_array))
