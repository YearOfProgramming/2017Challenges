## Solution for challenge 2
First, pull in my methods file. It includes the method that find the unique number.
Run that method on the array.

## The method: find_unique
Create a `count` hash. Iterate through the `nums` array, and for each number iterated through, add 1 to that numbers tally. Search through the hash for the element that has a value of 1, then return that elements key