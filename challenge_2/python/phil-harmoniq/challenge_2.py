int_array = [2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7]
mix_array = [2, 'a', 'l', 3, 'l', 4, 'k', 2, 3, 4, 'a', 6, 'c', 4, 'm', 6, 'm', 'k', 9, 10, 9, 8, 7, 8, 10, 7]
# scoping mistake on results.

def find_single(array):
    answer = []
    results = {}
    for i in array:
        if i in results.keys():
            results[i] += 1
        else:
            results[i] = 1

    for i, v in results.items():
        if v == 1:
            answer.append(i)

    print results
    return(answer)

print(find_single(int_array))
print(find_single(mix_array))
