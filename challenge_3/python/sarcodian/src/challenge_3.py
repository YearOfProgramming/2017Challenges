def majority(array0):
    store = {}
    for i in array0:
        store[i] = store.get(i,0) + 1
    
    for i in store.keys():
        if store[i] > len(array0)//2:
            return i
    print('No majority found')
