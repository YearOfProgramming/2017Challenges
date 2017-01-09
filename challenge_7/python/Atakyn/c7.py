# find the missing number in an list


def find_missing_number(array):
    n = len(array)
    should_be = (n / 2) * (n + 1)  # this is what the sum should be
    actual_sum = 0  # this is what the sum is
    for i in array:
        actual_sum += i
    return should_be - actual_sum


find_missing_number([0, 2, 3, 4, 1, 8, 7, 6, 5, 9, 11, 10, 12, 13, 15])
