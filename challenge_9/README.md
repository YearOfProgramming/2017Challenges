Squares
=======
Idea
-----
You are given an array of integers. The array will be sorted and may contain negative values. The array will go from least to greatest. Your job is to square everything in the array, then resort it. No problem right? Just a simple for loop to square every element, if that and call .sort or something right? Nope. The array must be resorted in O(N) time. 

Example: [-2,-1,0,1,2] should be returned from your function as [0,1,1,4,4]. 

[0,1,2] -> [0,1,4]

[-5,-4,-3,-2] -> [4,9,16,25]

[1,2] -> [1,4]

Notes
* The array will always be sorted before being passed into your function
* The array may or may not contain negative values
* The array may or may not contain 0
* The array may or may not contain positive values
* The array will not be empty

Hint: There is no limit to the space complexity for this challenge.

Testing
-----
Testing is rather straightforward. Simply create an array with/without negatives, 0 and positives, then feed it into your function and verify it by hand.