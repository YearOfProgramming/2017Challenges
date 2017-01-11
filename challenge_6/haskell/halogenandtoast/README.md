# Ranges

## 1. Approach

For this problem I decided the best solution would be to utilize the fact the
the numbers should be in order. So for a given array we know the front of the
array contains a range if we can take the first value and every value after it
is equal to the original value when we subtract it's index. To get the index
for each element, I utilize the fact that Haskell is lazy and I zip the tail
with a range from 1 to infinity.

## 2. Running

This challenge has no main function and instead you should run the tests

## 3. Testing

In order to run this you will need the `runhaskell` binary. Then you simply run

`runhaskell Spec.hs`

## 4. Overview of Code

### Challenge.hs

This file contains 3 helper functions and the core function `ranges`

`safeLast` is a helper method I wrote to return the last element of an array. If the array is empty it returns `Nothing`

`rangeStr` takes two numbers and formats them into a String. I could have introduced a new type `Range` that had an instance of Show, but I figured this would be overkill.

`endOfRange` this is the most complex function in my code, it takes an array and based on the first element returns a tuple containing the index and value of the last element that is part of the range of the first element of the array. It's possible the first element is not part of a range, and in that case it must return `Nothing`. To accomplish this task I zip the tail of my array with an infinite range from 1 to infinity. So if my tail was `[2,3,5]`, I'd have a lazily evaluated list of tuples in the form `[(1,2), (2,3), (3,5)]` then I use `takeWhile` to get the elements that meet the condition that the head element plus the index should equal the value in the tuple. So for the tuple `(1,2)` this holds true because `1 + 1 == 2`. For the tuple `(3,5)` this doesn't hold true though because `1 + 3 != 5`.

`ranges` combines our input with an empty array (the accumulator) and if the input is empty it returns the accumulator. Otherwise, if it find an ending value for the range it drops all the elements that are part of the range, adds our range string to our accumulator, and recurses. If there was no end of range, then the current element isn't part of a range and the code recurses on the tail while not modifying our accumulator.

### Spec.hs

This file contains a couple of simple tests to check that our `ranges`
functions works as expected.
