import numpy as np

def findMissing(l):
    n = len(l)
    return n*(n+1)/2 - np.sum(np.array(l))
    
if __name__=="__main__":
    t1 = [0,1,2,4];
    print "Input: ", t1
    print "Output: ", findMissing(t1)
    t2 = [1,2,3];
    print "Input: ", t2
    print "Output: ", findMissing(t2)
    t3 = [1,3,4,0];
    print "Input: ", t3
    print "Output: ", findMissing(t3)