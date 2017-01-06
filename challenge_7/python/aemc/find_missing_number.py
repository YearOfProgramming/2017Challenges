#!/usr/bin/env python3


def find_missing_number(num: list) -> int:
    total_from_num, total_from_indexes = 0, 0

    # go through every number in num and add it to total_from_num
    for i in num:
        total_from_num += i

    # Iterate through the range of len(num) +1 to aquire the number the total should be
    for i in range(1, len(num)+1):
        total_from_indexes += i

    # subtract the sum of the elements in the list from what the sum should be to obtain the number that's missing
    return total_from_indexes - total_from_num


if __name__ == '__main__':
    print(find_missing_number([5,4,3,2,1,8,7,6]))
