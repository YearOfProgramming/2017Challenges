def pick_char(array0):
    '''
    array0: list, the array that is entered with one unique char
    returns: char, a single element string or int that was unique in the array
    '''
    unique = []
    duplicate = []
    for i in array0:
        if i in duplicate:
            pass
        elif i in unique:
            duplicate.append(i)
            unique.remove(i)
        else:
            unique.append(i)
    return unique[0]

print(pick_char([2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]))