#!/usr/bin/env python3


def find_missing_number(nums):
    # sort list first and assign it to new variable called newlist
    newlist = sorted(nums)
    return sum(xrange(len(newlist)+1)) - sum(newlist) 


if __name__ == '__main__':
    print(find_missing_number([5,4,7,1,8,2,6,0]))

