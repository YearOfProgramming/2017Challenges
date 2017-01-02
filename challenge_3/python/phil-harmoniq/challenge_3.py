int_array = [2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7,
             7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7, 7, 7, 7]
results = {}


def find_majority(array):
    for i in array:
        if i in results.keys():
            results[i] += 1
        else:
            results[i] = 1

    for i, v in results.items():
        if v >= len(array) / 2:
            answer = i

    return(answer)


print(find_majority(int_array))
