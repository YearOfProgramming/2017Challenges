#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from collections import defaultdict


def main():
    if len(sys.argv) == 1:          # Arguments provided by piping in shell
        args = sys.stdin.read()
    elif len(sys.argv) == 2:        # Arguments provided as command line args
        args = sys.argv[1]
    else:
        print("Error: too many arguments")
        exit(1)

    inlist = args_to_list(args)
    test_digit(inlist)

    # Map elements to a dictionary where the key is the element and increment
    # the value (default value is 0 for each key initially)
    sum_dict = defaultdict(int)
    for elem in inlist:
        sum_dict[elem] += 1

    result = []
    majority_threshold = len(inlist) / 2

    for key, value in sum_dict.items():
        if value > majority_threshold:
            result.append(key)

    if result:
        print(result[0])
    else:
        print("No majority value found")


def args_to_list(arg_string):
    """ Parses argument-string to a list
    """
    # Strip whitespace -> strip brackets -> split to substrings ->
    # -> strip whitespace
    arg_list = [x.strip() for x in arg_string.strip().strip("[]").split(',')]
    return arg_list


def test_digit(arr):
    """ Exits if list contains non-numeric strings
    """
    for element in arr:
        if not element.isdigit():
            print("Error: '{}' is not numeric.".format(element))
            exit(1)

if __name__ == "__main__":
    main()
