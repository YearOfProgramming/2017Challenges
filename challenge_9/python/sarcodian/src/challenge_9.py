def square_n_sort(L):
    '''
    Get an ordered list of ints and square the values, returning a list
    of squares ordered from smallest to largest.
    '''

    L_square = []
    L_sorted = []
    count = len(L)

    if L[0] >= 0:
        for i in L:
            L_square.append(i**2)
        return L_square
    
    while count > 0:
        if abs(L[0]) >= abs(L[-1]):
            L_square.append(L[0]**2)
            L.remove(L[0])
        else:
            L_square.append(L[-1]**2)
            L.remove(L[-1])
        count -= 1

    L_sorted = L_square[::-1]
    
    return L_sorted