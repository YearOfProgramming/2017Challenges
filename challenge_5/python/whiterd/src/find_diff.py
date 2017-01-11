#!/usr/bin/env python

'''
    Input: string (series of characters) 

    Process: string input is randomly sorted and and additional character
        is added.
        
    Output: the additional character that is not present in the input.
'''

from __future__ import print_function
from random import shuffle, choice
from string import ascii_lowercase

def get_input():
    """Asks user for input and returns a string."""
    return str(input('Enter a series of unique characters: '))

def add_char(s):
    """Takes a string as input, adds a char, shuffles it, and returns
    the new string."""
    t = list(s)
    other_letters = set(ascii_lowercase) - set(t)
    t.append(choice(list(other_letters)))
    shuffle(t)
    return ''.join(t)
    
def find_diff(s, t):
    """Takes two strings as input and returns the differing character."""
    for i in t:
        if i not in s:
             return i


if __name__ == '__main__':

    s = get_input()
    print('You entered: ' + s)
    t = add_char(s)
    print('The newly generated string is: ' + t)
    print('The different character generated is: ' + find_diff(s, t))
