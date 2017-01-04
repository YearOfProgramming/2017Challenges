from collections import Counter

arr = [2, 'a', 'l', 3, 'l', 4, 'k', 2, 3, 4, 'a', 6, 'c', 4, 'm', 6, 'm', 'k', 9, 10, 9, 8, 7, 8, 10, 7]

print(list(Counter(arr).keys())[list(Counter(arr).values()).index(1)])

