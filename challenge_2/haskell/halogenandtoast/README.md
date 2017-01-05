# Single Number

## 1. Approach

My solution to this problem was to convert the array into a structure that
contains the important information. By converting the array into a HashTable -
O(n log n) because alter is O(log n) - I can easily keep track of the counts for
each element. Once the table is built I can filter it in order to get the value
I'm looking for.

Since Haskell requires that lists be Homogeneous I treat all values as strings
instead of Integers and Chars which solves both the first and second problems
of this challenge.

## 2. Running

In order to run this you will need the `runhaskell` binary. Then you simply run

`runhaskell Main.hs 1 1 2 2 3 4 3 a a`

## 3. Testing

In order to run this you will need the `runhaskell` binary. Then you simply run

`runhaskell Spec.hs`

## 4. Overview of Code

### Main.hs

This file contains the boilerplate to read values from STDIN. It passes these
values to `solve` located in `Challenge.hs` and prints the result

### Challenge.hs

This is the core of the code and includes two functions `counts` and `solve`.

`counts` will take an array of strings and return a hash whose keys are
elements of the array passed in and whose values are the number of times an
element in that array occurs. In order for this function to work we generate an
empty HashTable and pass that down to another function `counts'` which pattern
matches our array of values. On an empty array we know we are finished and
return the HashTable by calling the `id` function (id x = x). Otherwise we
update our hash and recursively call our function with the tail of the array.

`solve` gets the resulting counts and then filters our hash to contain only the
keys whose values (counts) are 1. Since we assume there is only matching result
we get the first element of our table and return that.

### Spec.hs

This file contains a couple of simple tests to check that our two functions
work correctly.
