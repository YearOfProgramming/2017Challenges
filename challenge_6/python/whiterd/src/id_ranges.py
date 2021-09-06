#!/usr/bin/env python

"""
    Identify the ranges that exist for a given input.

    Assume: input is a non-empty list of ordered integers.
"""
from __future__ import print_function

def range_finderer(new_list):
    result = []
    temp = []
    for i in new_list:
        if not temp:
            temp.append(i)
            continue
        elif(i - 1 == temp[-1]):
            temp.append(i)
            continue
        else:
            result.append(str(temp[0]) + '->' + str(temp[-1]))
            temp = [i]
    result.append(str(temp[0]) + '->' + str(temp[-1]))
    return result


if __name__ == '__main__':

    x = [int(x) for x in input('Input a list of integers: ')[1:-1].split(',')]
    print(range_finderer(x))
