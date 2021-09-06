def reorder(lst):
    res = [None] * (len(lst))
    
    for i in range(0,len(lst)):
        lst[i] = lst[i] ** 2
        
    
    i = 0
    j = len(res) - 1
    index = len(res) - 1
    
    while(i <= j and index >= 0):
        if(lst[i] > lst[j]):
            res[index] = lst[i]
            i += 1
        elif(lst[i] < lst[j]):
            res[index] = lst[j]
            j -= 1
        elif(lst[i] == lst[j]):
            res[index] = lst[i]
            if(index > 0):
                index -= 1
                res[index] = lst[j]
            i += 1
            j -= 1
            
        index -= 1
        
    return res