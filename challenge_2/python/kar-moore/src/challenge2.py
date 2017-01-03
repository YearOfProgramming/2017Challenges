def single_number(array):
    num_dict = {}
    for num in array:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
            
    for element in num_dict:
        if num_dict[element] == 1:
            return element

print single_number([1,2,2,3,3,3,1,4])
