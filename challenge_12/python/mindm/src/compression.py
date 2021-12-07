#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


def sub_com(matchobj):
    """ Calculates the compressed string from the first letter of the match
        and the length of the match
    """
    letter = matchobj.group(0)[0]
    length = len(matchobj.group(0))
    return "{}#{}".format(letter, length)


def sub_def(matchobj):
    """ Decompresses the match by multiplying the first character by the
        digit after the hash character
    """
    letter = matchobj.group(0)[0]
    length = int(matchobj.group(0)[2:])
    return "{}".format(letter * length)


def compress(input):
    """ Compresses string using 're'-library
    """
    out = re.sub(r'(.)\1\1\1+', sub_com, input)
    return out


def decompress(input):
    """ Decompresses string using 're'-library
    """
    out = re.sub(r'([A-Za-z]#\d+)', sub_def, input)
    return out
