# Challenge 5: Find the Difference

## Running it

Compile with cabal, and then type `cabal exec challenge5 STRING1 STRING2`.

## Method

Perhaps the simplest possible solution would be to sort both strings and then
find the first difference. However, a more efficient solution is obtained by
using a 26-element array to count the characters in both strings and then
finding the count which differs. This method runs in `O(n)` as opposed to the
`O(n log n)` running time of the simpler solution.

## Implementation details

Haskell has at least three different standard string types; we here use
`ByteString`, since `String` is inefficient for most purposes and `Text` is for
Unicode, which we don't care about.

We also use the `vector` package rather than Haskell's built-in `Array` type.