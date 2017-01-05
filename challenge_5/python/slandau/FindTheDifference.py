#!/usr/bin/env python3


def findTheDifference(string1: str, string2: str) -> str:
    """
    Determines which letter(s) in string1 are not in string2.
    :param string1: The string that has one (or more) letters than string2
    :param string2: The string that has fewer letters than string1
    :return: The letters that are in string1 and not string2 or "string1 and string2 are identical"
    if they contain the same letters.
    """
    # Turn string1 into a list
    letters_s1 = list(string1)

    # Go through string2 and remove any characters in string1 that appear in string 2.
    # As far as I know the .remove only removes the first instance of that character.
    # This solves the problem of having more than one of any character in a string
    for char in string2:
        letters_s1.remove(char)

    if len(letters_s1) > 0:
        return 'The letters in string1 that are not in string2 are: ' + "".join(letters_s1)
    elif len(letters_s1) == 0:
        return 'string1 and string2 have the same letters (and number of each letter)'
    else:
        return 'Invalid input. string1 must be greater than or equal to string2.'


if __name__ == '__main__':
    print(findTheDifference('hello', 'hell'))