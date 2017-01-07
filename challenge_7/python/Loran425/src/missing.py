def find_missing_number(lst):
    actual = sum(lst)                         # O(1) space and O(n) complexity
    expected = len(lst) * (len(lst) + 1) / 2  # sum equation
    return expected - actual


