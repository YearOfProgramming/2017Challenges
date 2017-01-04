from collections import defaultdict

def find_unique(sequence):
    counter_dict = defaultdict(int)
    uniques = []

    for item in sequence:
        counter_dict[item] += 1

    for item, count in counter_dict.items():
        if count == 1:
            uniques.append(item)

    return uniques

test_sequence_list = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]

print(find_unique(test_sequence_list))

