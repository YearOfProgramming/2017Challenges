from collections import Counter

counter = Counter((2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7))
dict_ = dict(counter)

for k, v in dict_.items():
    if v == 1:
        print(k)
