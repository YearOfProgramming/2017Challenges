from collections import Counter

array = [2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7, 7,
         7, 7]

print(list(Counter(array))[list(Counter(array).values()).index(max(list(Counter(array).values())))])
