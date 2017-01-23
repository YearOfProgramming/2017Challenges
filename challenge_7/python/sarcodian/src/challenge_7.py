def missing_int(L):
    '''
    Ask for a list and return the missing value
    '''

    sum_n = 0
    sum_n_less_1 = 0

    for i in range(len(L)+1):
        sum_n += i
    
    for i in L:
        sum_n_less_1 += i

    return sum_n - sum_n_less_1


