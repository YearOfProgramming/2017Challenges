def brackets():
    '''
    Asks for a string and returns True/False.
    True if all openning brackets {([ have a matching ])},
    else returns False
    '''
    
    a_string = input("Please enter a string to process: ")

    brac_dict = {
        '}' : '{',
        ']' : '[',
        ')' : '(',
    }

    brac_store = []

    for i in a_string:
        if i in brac_dict.values():
            brac_store.append(i)
        elif i in brac_dict.keys():
            if len(brac_store) == 0:
                return False
            if brac_dict[i] == brac_store[-1]:
                del brac_store[-1]
            else:
                return False
            
    if len(brac_store) > 0:
        return False
    else:
        return True