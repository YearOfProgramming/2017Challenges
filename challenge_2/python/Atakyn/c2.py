# find the non-repeating integer in an array
# set operations (including 'in' operation) are O(1) on average, and one loop that runs n times makes O(n)


def single(array):
    repeated = set()
    not_repeated = set()
    for i in array:
        if i in repeated:
            continue
        elif i in not_repeated:
            repeated.add(i)
            not_repeated.remove(i)
        else:
            not_repeated.add(i)
    return not_repeated

array1 = [2, 'a', 'l', 3, 'l', 5, 4, 'k', 2, 3, 4, 'a', 6, 'c', 4, 'm', 6, 'm', 'k', 9, 10, 9, 8, 7, 8, 10, 7]
print(single(array1))  # {'c', 5}
