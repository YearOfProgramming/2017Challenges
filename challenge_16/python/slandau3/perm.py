#!/usr/bin/env python3
import math
lst = []

def perm(string, chr):
    if len(chr) == 0:
        print(string)
        lst.append(string)
        return
    for i in range(len(chr)):
        c = chr[i]
        otherstring = chr[:i] + chr[i+1:]
        perm(string + c, otherstring)


perm("", "abcdefghi")
print(lst)
print(len(lst))