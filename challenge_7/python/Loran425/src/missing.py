def find_missing_number(lst):
    actual = sum(lst)                         # O(1) space and O(n) complexity
    expected = len(lst) * (len(lst) + 1) / 2  # sum equation
    return expected - actual


if __name__ == '__main__':
    numbers = [0, 7, 8, 3, 5, 6, 1, 9, 4] # missing the number 2
    print("The number {} is missing from the input list".format(find_missing_number(numbers)))
