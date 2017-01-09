# Squares

This algorithm takes an array of sorted integers and returns a sorted array of 
doubles that equal the square of every element in the provided array.  This 
solution runs in O(N) time and uses O(N) space. 

The idea is to split the original array into two: `positives` and `negatives`. The
`positives` array should be sorted with the smallest element first; the `negatives`
array should be sorted with the largest element first.  

Once the arrays are sorted each entry can be squared; after this operation we
know that `positives` and `negatives` are sorted in ascending order.  To get 
the `result` array perform a merge sort on `positives` and `negatives`.