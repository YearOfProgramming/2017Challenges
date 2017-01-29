The code accept a list of ordered integer.
We look in the list for groups of consecutive number and we will give as output 
the starting point and the end point.

To perform this task we start from the beginning of the list and we will check if the next
element is *considered_element +1. If it is a consecutive element we move to the next one otherwise we record the index of the last element that we analyzed. 
If this index is different from the starting point we will print the range.