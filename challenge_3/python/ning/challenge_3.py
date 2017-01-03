def find_majority(sequence):
    item_counter = dict()

    for item in sequence:
        if item not in item_counter:
            item_counter[item] = 1
        else:
            item_counter[item] += 1

    for item, item_count in item_counter.items():
        if item_count > len(sequence) / 2:
            return item

test_sequence_list = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]

print(find_majority(test_sequence_list))

