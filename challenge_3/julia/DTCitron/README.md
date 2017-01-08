#Majority Element

##Premise

-	Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

-	You may assume that the array is non-empty and the majority element always exist in the array.

for example, given array = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7] your program should return 7


## Implementation

- Call 'julia majority.py' in the 'src' directory to return the majority element from the sample array
- The majority() function uses a dictionary ('counter') to count the number of times each element appears in the input array
- If a majority element does not exist, returns a message stating that there is no such element
- More on dictionaries here: https://en.wikibooks.org/wiki/Introducing_Julia/Dictionaries_and_sets
