def maj_element(array):
    maj = len(array)/2 #python does flooring on int division
    num_dict = {}
    for num in array:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    for element in num_dict:
        if num_dict[element] >= maj:
            return element


array = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,
7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7] \

print maj_element(array)

b_array = [1,1,2,2,2,2,2]

print maj_element(b_array)