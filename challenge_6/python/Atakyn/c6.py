# find the ranges in a list


def ranges(array):
    if array is None or len(array) == 0:
        return []
    start = [array[0]]
    end = []
    last = array[0]
    for i in array[1:]:
        if last + 1 != i:
            end.append(last)
            start.append(i)
        last = i
    start.append(last)
    end.append(array[-1])

    result = []
    for s, e in zip(start, end):
        if s != e:
            result.append(f'{s}->{e}')

    return result


print(ranges([5, 6, 9, 10, 12, 13, 15, 16, 18, 19, 25, 30]))
print(ranges([]))
