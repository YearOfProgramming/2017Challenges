def find_missing_number(c):
    b = max(c)
    if min(c) == 1:
        d = min(c + [0])
    else:
        d = min(c)
    v = set(range(d, b)) - set(c)
    return v if v != set() else None

print(find_missing_number([1, 3, 2, 4]))
print(find_missing_number([0, 2, 3, 4, 5]))
print(find_missing_number([9, 7, 5, 8]))
