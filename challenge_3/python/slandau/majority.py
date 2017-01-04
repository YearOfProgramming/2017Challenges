#!/usr/bin/env python3


def majority(input: list) -> str:
    # Create a dictionary of occurrences, mapping a character to a value
    occurences = {}
    # Go through the input and fill the dictionary
    for i in input:
        if occurences.get(i, None) is None: # O(1) access to the dictionary (even if the key does not exist)
            occurences[i] = 1
        else:
            occurences[i] += 1

    # majority_occurrence will be the largest occurrence of a character we have yet to see
    majority_occurrence = 0
    # majority_char will be the character associated with majority_occurrence
    majority_char = ""
    for i in occurences:
        if occurences[i] > majority_occurrence:
            majority_occurrence = occurences[i]
            majority_char = i

    return majority_char


if __name__ == '__main__':
    print(majority([2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]))