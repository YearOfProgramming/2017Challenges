# Challenge #10, Valid Closers

I found three cases where the sequence can be considered to have 'invalid closers'.

1. A mismatch in the number of opening and closing brackets, e.g. `())`
2. Premature closing, e.g. `][`
3. Overlapping of brackets, e.g. `([<)]>`

In this solution, we use a list to 'count' the brackets as we iterate through the list. Every opening bracket adds to this list `mem`, and closing brackets remove their corresponding openings from the list.

The first invalid case is partially tested for by checking if the list `mem` is empty at the end of the iteration. The works for an abundance, but not shortage of opening brackets.

For the case whereby there is a shortage of closing brackets, we simply return False in the case of an `IndexError`. This also covers the second case of premature closing.

For the third case of overlapping, we check for every closing bracket if the most recent _unclosed_ opening bracket is of the same type. If not, False is returned as expected.

The unit test, `test.py`, is constructed simply from the examples given.

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```
