# Challenge # 2
# 2017 Programming Challenge @ Slack
# 
# Single Number
# ------------------------------------------

# Premise
#
# For this coding challenge you are given an array of random integers where
# every integer is repeated except for a single one. Your challenge is to
# find the single integer that does NOT repeat.
# example: given array = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7] your program
# should return: 5
#
# Assume that the array can hold infinitely many integers. Can you make your
# solution run in linear time O(n)? Good luck!
#
# attempt to search through array with characters extra credit:
# given array= [2,a,l,3,l,4,k,2,3,4,a,6,c,4,m,6,m,k,9,10,9,8,7,8,10,7]
# your program should return: c, 5

# Language: Python 3.6

print ("Welcome to Single Number Array")
numberofItems = int(input ("Please enter the lenght of your array: "))
userArray = []
nonDup = []
if numberofItems != 0:
    i = 0
    while i < numberofItems:
        userValue =  (input ("Enter a new value to the array: "))
        if userValue not in userArray:
            nonDup.append(userValue)
        elif userValue in nonDup:
            nonDup.remove(userValue)
        userArray.append(userValue)
        i += 1
    print ("Here is your Array: " , userArray)
    print ("Here are the single values: " , nonDup)
else:
    exit    


