def missing_int(L):
    '''
    Ask for a list and return the missing value
    '''

    sum_n = 0
    sum_n_less_1 = 0

    for i in range(len(L)+1):
        sum_n += i
    
    sum_n_less_1 = sum(L)

    return sum_n - sum_n_less_1


