def majority(s):
    # Create a counter dictionary {element of s : number of times it appears in s}
    counter = dict()
    length_s = 0
    # Count the number of times each element of s appears
    for i in s:
        length_s += 1
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
   # Loop through the items in the counter dictionary, return majority element
    for t in counter.items():
        if t[1] > length_s/2.:
            return t[0]
    # If no majority element, return a message:
    return "No majority element"


if __name__=="__main__":
    # Example case from the prompt
    print majority([2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7])
    # Another case
    print majority([1,1,1,2,3,4,1,1,1])
    # And a case with no majority
    print majority([9,9,9,9,8,8,8,8])
