from collections import defaultdict

def unique(lst):
    # Super duper lazy way of solving problem... o(n^2) method.
    unique_lst = [itm for itm in lst if lst.count(itm) == 1]
    return unique_lst

def unique_v2(lst):
    """
    Returns a list of all unique elements in the input list "lst."
    This algorithm runs in o(n), as it only passes through the list "lst" twice
    """
    dd = defaultdict(int) # avoids blank dictionary problem (KeyError when accessing nonexistent entries)
    unique_list = []
    for val in lst:
        dd[val] += 1
    for val in lst:
        if dd[val] == 1:
            unique_list.append(val)
    return unique_list