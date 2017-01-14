#!/usr/bin/env python

'''
    Input:  An array of random integers where every integer is repeated except
    for a single one.

    Output:  The single integer that does NOT repeat.
'''

from __future__ import print_function

array_1 = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
array_2 = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]

def find_distinct(array):
    for i in array:
        if array.count(i) == 1:
            return i


if __name__ == '__main__':
    print(find_distinct(array_1))
    print(find_distinct(array_2))
