# Squares
---
- O(n)
- Uses Int stack to keep track of squares from negative numbers (implemented
    as list)

Uses an index to scan through `ints` and `squares`, when encountering a negative
number in `ints`, it pushes the current value from `squares` onto the mentioned
Int stack.

Otherwise, when either `currIndex == squares.length` or the current top of the
Int stack is `>= squares(currIndex)`, the Int stack is popped, and the top item
is added to the solution. Otherwise, `squares(currIndex)` is simply added to the
solution.
