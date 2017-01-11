array = [2,5,4,2,3,5,4,6,4,6,'d',9,10,9,8,7,8,10,7,3,11,'d',11,'c', 21]
pos = 0
# Returns bool and position in array if single == true
def scan(ar):
    single = True
    for i in xrange(len(ar)):
        if (ar[i] == ar[pos]) and (i != pos):
            return False, 0

    return True, pos

for pos in xrange(len(array)):
    suc, val = scan(array)
    if (suc):
        print "Non repeating value:", array[val]
    else:
        continue
