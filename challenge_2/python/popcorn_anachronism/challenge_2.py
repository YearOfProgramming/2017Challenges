array = list(input().split(","))

def find_single(array):
    for item in array:
        if array.count(item) == 1:
            return item

print(find_single(array))
