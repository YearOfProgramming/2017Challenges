#!/usr/bin/env python

"""
#Reverse a String

##Premise

-	For this coding challenge, your task is to reverse a string for any given
    string input.

Example: Given s = "hello", return "olleh".

-	Try to make the solution as short and simple as possible in your respective
    language of choice.
"""


def reverse_string(string):
    return ''.join([string[idx - 1] for idx in range(len(string), 0, -1)])


if __name__ == '__main__':
    str_to_reverse = 'easy as abc'
    print 'Before: ', str_to_reverse
    print 'After: ', reverse_string(str_to_reverse)
