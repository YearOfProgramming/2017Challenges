#! /usr/bin/python3
"""Challenge 1 in Python."""
# coding: utf-8

s = "hello"

for i in range(len(s) - 1, -1, -1):
    print(s[i], end='')
