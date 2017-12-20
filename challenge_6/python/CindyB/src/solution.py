def ranges(values):
    found_ranges = []
    first_number = values[0]

    for index in range(1,len(values)):
        if (values[index] - 1 != values[index-1] and first_number != values[index-1]):
            found_ranges.append(str(first_number) + "->" + str(values[index-1]))
            first_number = values[index]
    
    return found_ranges