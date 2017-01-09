#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_difference(string1, string2):
    """ Find the differing character between strings.
        string2 must be one character longer than string1.
    """
    assert len(string1) + 1 == len(string2)

    char_array = list(string2)

    # Iterates through the first string, popping characters out of the second
    # string until there is only 1 character left
    for char in string1:
        ind = char_array.index(char)
        char_array.pop(ind)

    return char_array[0]
