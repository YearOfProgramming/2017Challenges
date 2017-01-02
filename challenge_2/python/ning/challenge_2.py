def find_unique(sequence):
    item_counter = dict()
    uniques = list()

    for item in sequence:
        if item not in item_counter:
            item_counter[item] = 1
        else:
            item_counter[item] += 1

    for item, item_count in item_counter.items():
        if item_count == 1:
            uniques.append(item)

    return uniques

test_sequence_list = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]

print(find_unique(test_sequence_list))

