#!/usr/bin/env python3
# @author slandau3


def reorder(input: list) -> list:
    neg_index, pos_index = find_neg_and_pos_index(input)

    # Square the list. Can also be done with a list comprehension (probably)
    for i in range(len(input)):
        input[i] **= 2

    re_ordered = []

    # This is the part where we go through the square list and essentially re order it.
    # We kept track of the index where the least negative integer was so we can re order this in O(N) time
    # Think about it this way [-3, 0, 2]. neg_index would be 0 and pos_index would be 1.
    # The squared list would be [9, 0, 4]
    # We would now compare 9 and 0, we see that 0 is smaller so that gets appended to re_ordered first.
    # We then increment pos_index so it is now  2 (which equals 4 in this case)
    # we now compare 4 and 9 and see that 4 is smaller so that gets appended to re_ordered
    # Go around again and append 9
    while len(re_ordered) != len(input):
        if input[neg_index] < input[pos_index]:
            # if the input at negative index is smaller, append input[neg_index] to the new list
            re_ordered.append(input[neg_index])
            neg_index -= 1
        elif input[neg_index] >= input[pos_index]:
            # if the input at both indexes is the same or pos_index's value is smaller
            # append input[pos_index] to re_ordered
            re_ordered.append(input[pos_index])
            if pos_index != len(input)-1:
                # We don't want to get an index out of bounds error so don't do anything if we hit
                # the last value
                pos_index += 1

    return re_ordered


def find_neg_and_pos_index(sorted_list: list):
    """
    Finds the least negative, negative value and the least positive, positive value (including 0).
    :param sorted_list: The (un-squared) input list
    :return: The negative index and positive index
    """
    neg_index = 0
    pos_index = 0
    pos_evaluated = False
    for i in range(len(sorted_list)):
        if sorted_list[i] < 0: # find the least negative, negative number
            neg_index = i
        if sorted_list[i] >= 0 and not pos_evaluated: # Find the least positive positive number
            # This includes 0
            pos_index = i
            pos_evaluated = True

    if sorted_list[neg_index] == 0:
        neg_index = len(sorted_list)

    return neg_index, pos_index

if __name__ == '__main__':
    print(reorder([-100,-50,-2,-1,80,900,9001]))

