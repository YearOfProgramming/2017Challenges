## Solution for challenge 2
First, require my methods file. It includes an `ElementsArray` class, which includes the method that finds the unique number.
Create a new `ElementsArray` object in the `nums` variable, and pass into the constructor an array of integers. This array will be named `@elements`.
Run the `find_unique` method on the array.

## The method: find_unique
Create a `count` hash. Iterate through the `@elements` array, and for each number iterated through, add 1 to that numbers tally. Search through the hash for the element that has a value of 1, then return that element's key