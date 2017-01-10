"""
Takes a list of sorted integers, squares all the numbers and sorts the new list.
Ex.
Input = [-2, 0, 4, 7]
Output = [0, 4, 16, 49]
"""


def square_sort(inp: list) -> list:
    pos, neg = [], []
    for i in inp:
        pos.append(i**2) if i >= 0 else neg.append(i ** 2)
    neg = neg[::-1]

    result = []

    while pos != [] and neg != []:
        if pos[0] > neg[0]:
            result.append(neg.pop(0))
        else:
            result.append(pos.pop(0))

    return result + pos if neg == [] else neg

print(square_sort([1, 4, 6, 8, 8]))
print(square_sort([0, 2, 6, 8]))
print(square_sort([-3, 0, 1, 6]))
print(square_sort([-2, -1, 0, 6]))
print(square_sort([-2, 3]))
