test1 = [0,1,2,4]           #answer: 3
test2 = [9,6,7,8,5,4,1,3,0] #answer: 2
test3 = list(range(100000)) #answer: 99 
test3.remove(99)

def find_missing(array):
    return sum(range(len(array)+1))-sum(array)
        
print(find_missing(test1))
print(find_missing(test2))
print(find_missing(test3))
