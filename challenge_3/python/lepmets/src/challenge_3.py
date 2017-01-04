#! /usr/bin/python3
"""Challenge #3 in Python."""
# coding: utf-8

array = [2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6,
         7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7, 7, 7, 7]

element_counts = {}

"""Find out how many of each number there is in 'array'
and store it in element_counts."""
for element in array:
    element_counts.setdefault(element, 0)
    element_counts[element] = element_counts.get(element) + 1

"""Loop over element_counts. If any number's count is greater than array
length/2 (n/2), print that number."""
for a in element_counts.keys():
    if element_counts.get(a) > len(array) / 2:
        print(a)
