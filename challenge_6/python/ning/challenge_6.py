def ranges(input_list):
    output_elements = list(input_list)  # copy, not assign
    input_lookup = set(input_list)
    output_list = []

    for integer in input_list:
        if (integer + 1 not in input_lookup and
            integer - 1 not in input_lookup):
            output_elements.remove(integer)
        elif (integer - 1 in input_lookup and
              integer + 1 in input_lookup):
            output_elements.remove(integer)

    for i, integer in enumerate(output_elements):
        if i % 2 == 0:
            output_list.append('{}->{}'.format(integer, output_elements[i+1]))
#            output_list.append(f'{integer}->{output_elements[integer+1]}')

    return output_list

