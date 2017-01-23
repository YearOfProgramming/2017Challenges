def compress():
    '''
    Ask for a string input and return a compressed string with all
    consecutive repetitions for 4 or greater replaced with a representation
    in the form of y#N.
    aaaaa -> a#5
    '''

    orig_string = input("Enter the list to compress: ")
    temp = ''
    comp_string = ''

    for i, j in enumerate(orig_string):
        try:
            if j != orig_string[i+1]:
                temp += j
                if len(temp) > 4:
                    comp_string += '{}#{}'.format(temp[0], len(temp))
                    temp = ''
                else:
                    comp_string += j
                    temp = ''
            else:
                temp += j
        except IndexError:
            if j == orig_string[i-1]:
                temp += j
                if len(temp) > 4:
                    comp_string += '{}#{}'.format(temp[0], len(temp))
                    temp = ''
                else:
                    comp_string += temp
                    temp = ''
            else:
                temp += j
    if len(temp) > 0:
        comp_string += temp

    return comp_string

def decompress():
    '''
    Ask for a string and expand all instances of #N with the char preceeding it
    repeated N times.
    a#5 -> aaaaa
    '''
    comp_string = input("Enter string to be decompressed: ")
    temp = ''
    orig_string = ''

    for i, j in enumerate(comp_string):
        if j in '0123456789':
            pass
        elif j == '#':
            num = i+1
            while comp_string[num] in '0123456789':
                temp += comp_string[num]
                num += 1
            orig_string += comp_string[i-1]*(int(temp)-1)
            temp = ''
        else:
            orig_string += j
    
    return orig_string
