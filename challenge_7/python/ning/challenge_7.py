def find_missing(input_list):
    input_set = set(input_list)
    for i in range(min(input_list), max(input_list)+1):
        if i not in input_set:
            return i

def alt_find_missing(input_list):
    input_sum = sum(input_list)
    range_sum = sum([i for i in range(min(input_list), max(input_list)+1)])
    return range_sum - input_sum
