# Find the Difference

## 1. Approach

This program works by creating an array large enough to store each letter of the alphabet (26) and then proceeds to count all the occurences. It then finds the character that has occured an odd number of times.

Because of how arrays work in Haskell I had to utilize the Lens library to update specific array elements.

## 2. Running

This challenge has no main function and instead you should run the tests

## 3. Testing

In order to run this you will need the `runhaskell` binary. Then you simply run

`runhaskell Spec.hs`

## 4. Overview of Code

### Challenge.hs

This is the core of the code and includes 3 helpers functions and the main `findTheDifference` function.

`toAlphaNum` is a helper function that takes a char and returns the letters index between 0 and 25 by calculating its ascii value and subtracting the ascii value of lowercase a

`fromAlphaNum` reverse what `toAlphaNum` does

`trackCharacters` takes an array of integers (representing the currently stored counts for each letter) and an array of characters. If the array of characters is empty it returns the counts, otherwise it calls itself recursively with an updated array of counts (incrementing via `succ` the cell that matches the head of string) and the tail of our string.

`findTheDifference` will first count the number of times each character in the alphabet occurs in both strings by calling `trackCharacters` twice (once for each string). Then we find which index has an odd number (if any) and use fmap `<$>` to return either `Nothing` or `Just Char`

### Spec.hs

This file contains a couple of simple tests to check that our `findTheDifference` functions
works as expected.
