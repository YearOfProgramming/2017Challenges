# Find the Missing Number

## 1. Approach

Here we utilize the trick that if we sum the numbers and subtract that from the sum we'd expect, we get the missing number. The number we expect is actually a [Triangle Number][triangle] and can be found with the forumula:

````
n * (n + 1)
-----------
    2
```

## 2. Running

This challenge has no main function and instead you should run the tests

## 3. Testing

In order to run this you will need the `runhaskell` binary. Then you simply run

`runhaskell Spec.hs`

## 4. Overview of Code

### Challenge.hs

The `missingNumber` function is fairly straight forward. First we calculate the triangle number and then we subtract from it, the sum of our array.

### Spec.hs

This file contains a couple of simple tests to check that our `missingNumber`
function works as expected.

[triangle]: https://en.wikipedia.org/wiki/Triangular_number
