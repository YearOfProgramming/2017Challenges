def pick_char(array0):
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