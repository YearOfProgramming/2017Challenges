def majority_element(array):
    half_time = len(array)/2
    for element in array:
        if array.count(element) > half_time:
            return element

# testing majority_element
array = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]
print(majority_element(array))
