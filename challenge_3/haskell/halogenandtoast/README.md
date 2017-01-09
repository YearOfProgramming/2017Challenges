# Majority Element

## 1. Approach

My solution to this problem was to convert the array into a structure that
contains the important information. By converting the array into a HashTable -
O(n log n) because alter is O(log n) - I can easily keep track of the counts for
each element. Once the table is built I can sort it based on frequency and
return the key with the highest frequency.

## 2. Running

In order to run this you will need the `runhaskell` binary. Then you simply run

`runhaskell Main.hs 1 1 2 2 3 4 1 1 1`

## 3. Testing

In order to run this you will need the `runhaskell` binary. Then you simply run

`runhaskell Spec.hs`

## 4. Overview of Code

### Main.hs

This file contains the boilerplate to read values from STDIN. It passes these
values to `findMajority` located in `Challenge.hs` and prints the result

### Challenge.hs

This is the core of the code and includes two functions `counts` and
`findMajority`.

`counts` will take an array of values and return a hash whose keys are elements
of the array passed in and whose values are the number of times an element in
that array occurs. In order for this function to work we generate an empty
HashTable and pass that down to another function `counts'` which pattern
matches our array of values. On an empty array we know we are finished and
return the HashTable by calling the `id` function (id x = x). Otherwise we
update our hash and recursively call our function with the tail of the array.

`solve` gets the resulting counts and then converts them to a list of tuples
(`toList`) and then sorts that list in descending order. We can then take the
head element of that list to find the majority.

### Spec.hs

This file contains a couple of simple tests to check that our two functions
work correctly.
