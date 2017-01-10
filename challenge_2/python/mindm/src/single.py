#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from collections import defaultdict


def main():
    if len(sys.argv) == 1:      # Arguments provided by piping in shell
        args = sys.stdin.read()
    elif len(sys.argv) == 2:    # Arguments provided as command line args
        args = sys.argv[1]
    else:
        print("Error: too many arguments")
        exit(1)

    inlist = args_to_list(args)
    
    if test_alnum(inlist) == False:
        print("Invalid arguments")
        exit(1)

    # Map elements to a dictionary where the key is the element and increment
    # the value (default value is 0 for each key initially)
    sum_dict = defaultdict(int)
    for elem in inlist:
        sum_dict[elem] += 1

    result = []

    for key, value in sum_dict.items():
        if value == 1:
            result.append(key)

    if len(result) == 1:
        print(result[0])
    elif len(result) > 1:
        print("Found more than 1 single value")
    else:
        print("No single values found")


def args_to_list(arg_string):
    """ Parses argument-string to a list
    """
    # Strip whitespace -> strip brackets -> split to substrings ->
    # -> strip whitespace
    arg_list = [x.strip() for x in arg_string.strip().strip("[]").split(',')]
    return arg_list


def test_alnum(arr):
    """ Returns false if list contains non-alphanumeric strings
    """
    for element in arr:
        if not element.isalnum():
            return False
    return True


if __name__ == "__main__":
    main()
