#! /usr/bin/python3
"""Challenge #2 in Python."""
# coding: utf-8


list_with_chars = [2, 'a', 'l', 3, 'l', 4, 'k', 2, 3, 4, 'a', 6,
                   'c', 4, 'm', 6, 'm', 'k', 9, 10, 9, 8, 7, 8, 10, 7]

list_with_numbers = [2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7]


def search_list(list_provided):
    """Search list provided for characters that are represented only once."""
    for i in range(len(list_provided) - 1):
        if not list_provided[i] in list_provided[i + 1:] and not list_provided[i] in list_provided[:i]:
            """If the same number is not present before or after in the list then
            return the number"""
            return str(list_provided[i])
            break


print(search_list(list_with_numbers) + ', ' + search_list(list_with_chars))
