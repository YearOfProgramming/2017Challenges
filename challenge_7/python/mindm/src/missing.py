#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_missing(input_list):
    """ Find the missing number in shuffled list
    """
    
    # Mathematical formula for finding the sum of consequtive natural numbers
    # (N*(N+1))/2
    total = (len(input_list) * (len(input_list) +1)) / 2
    
    summed = 0

    for element in input_list:
        summed += element

    missing = total - summed

    return missing
