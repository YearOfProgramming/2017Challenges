def ranges(int_list):
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
    print(final_list)
    return final_list

def print_range(range_list):
    return '{}->{}'.format(range_list[0], range_list[-1])
