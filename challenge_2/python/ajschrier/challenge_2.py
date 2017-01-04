array1 = [2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7]
array2 = [2, 'a', 'l', 3, 'l', 4, 'k', 2, 3, 4, 5, 'a', 6, 'c', 4, 'm', 6, 'm', 'k', 9, 10, 9, 8, 7, 8, 10, 7] # noqa


def singletonCharacters(array):
    candidateCharacters = []
    failedCharacters = []
    for i in array:
        if i not in failedCharacters:
            if i in candidateCharacters:
                candidateCharacters.remove(i)
                failedCharacters.append(i)
            else:
                candidateCharacters.append(i)
    return candidateCharacters

print singletonCharacters(array1)
print singletonCharacters(array2)
