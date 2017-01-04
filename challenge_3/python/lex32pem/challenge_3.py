# Challenge # 3
# 2017 Programming Challenge @ Slack
# 
# Majority Element
# 
# Premise
# 
# Given an array of size n, find the majority element. The majority element is the element
# that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always exist
# in the array.
# 
# for example, given:
# 
# array = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7]
# 
# your program should return 7
# 
# Language: Python 3.6

def find_Max(u):
    dictMax = {}                            # empty dictionary
    max = ('', 0)                           # (max element, max occurrences)
    for n in u:                             # to apply condition on each item of array in the defined function
        if n in dictMax:                    # if item already exist in dictionary
            dictMax[n] += 1                 # add 1 to the value of item [n] of array
        else:                               # if item doesnt exist in dictionary
            dictMax[n] = 1                  # value of item is 1
        if dictMax[n] > max[1]:             # also, if item on array is larger than max
            max = (n,dictMax[n])            # max item is updated with n and its value on the dictionary
    return max                              # new function return max

# Below the code for the user to enter the new array and apply the new function find_Majority

print ("Welcome to \"Majority Element\"")                               
print ("\"Majority Element\" is about find the element that appears more than 'n/2' in any given array of size 'n'")    
numberofItems = int(input ("Please enter the lenght of your array: "))  
userArray = []                                                          
majorityCondition = numberofItems/2                                     

if numberofItems != 0:                                                  
    i = 0
    while i < numberofItems:
        userValue =  (input ("Enter a new value to the array: "))
        userArray.append(userValue)
        i += 1
    print ("Here is your Array: " , userArray)

majArray = find_Max(userArray)

if majArray[1] > majorityCondition:
    print ("The majority element is: ", majArray[0], "with ", majArray[1], "occurrences. ")
else:
    print ("The element \"", majArray[0], "\" has the most ocurrences, but it doesn't appear more than 'n/2' in the given array")
    


