def find_unique_element(array):
    for element in array:
        if array.count(element)==1:
            return element

array = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
print(find_unique_element(array))

array = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]
print(find_unique_element(array))
