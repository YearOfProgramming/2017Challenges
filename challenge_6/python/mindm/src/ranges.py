#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_ranges(input_list):
    """ Find the differing character between strings.
        string2 must be one character longer than string1.
    """

    if len(input_list) == 0:
        return []

    start = None
    end = None
    previous = None
    range_list = []

    for num in input_list:
        if start is None:
            start = num
            previous = num
            continue

        if num == previous + 1:
            previous = num
            continue

        else:
            end = previous
            if start != end:
                range_list.append("{}->{}".format(start, end))
            start = num
            previous = num

    end = input_list[-1]

    if start != end:
        range_list.append("{}->{}".format(start, end))

    return range_list
