def find_missing(input_list):
    input_set = set(input_list)
    for i in range(min(input_list), max(input_list)+1):
        if i not in input_set:
            return i

