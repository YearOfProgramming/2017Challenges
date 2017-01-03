# find majority element in array
from collections import defaultdict


def find_majority_element(array):
    majority_value = len(array) // 2
    values = defaultdict(int)
    for e in array:
        values[e] += 1
        if values[e] > majority_value:
            return e


array1 = [2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7, 7,
          7, 7]
print(find_majority_element(array1))
