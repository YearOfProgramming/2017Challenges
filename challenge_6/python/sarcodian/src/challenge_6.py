def ranges(int_list):
    '''
    int_list: list, containing intergers sorted from low to high
    returns: list, each element is the first and last digit of a run
        of consecutive numbers with the middle digits replaced by an
        arrow.
    '''
    temp_list = []
    final_list = []

    if len(int_list) < 2:
        return []

    for i in range(len(int_list)):
        if i == len(int_list)-1:
            if int_list[i-1] == int_list[i]-1:
                temp_list.append(int_list[i])
                final_list.append(print_range(temp_list))
        elif int_list[i] == int_list[i+1]-1:
            temp_list.append(int_list[i])
        else:
            temp_list.append(int_list[i])
            final_list.append(print_range(temp_list))
            temp_list.clear()
    return final_list

def print_range(range_list):
    '''
    range_list: list, a list of consecutive integers
    returns: string, first and last integer with arrow in the middle
    '''
    return '{}->{}'.format(range_list[0], range_list[-1])
