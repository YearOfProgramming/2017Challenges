#!/usr/bin/env python3


def find_missing_number(nums):
	# Subtract the sum of nums of nth length from the sum of nums of nth + 1 length
	# nth + 1 is the list of numbers without a missing number
    return sum(xrange(len(nums)+1)) - sum(nums) 


if __name__ == '__main__':
    print(find_missing_number([5,4,7,1,8,2,6,0]))

