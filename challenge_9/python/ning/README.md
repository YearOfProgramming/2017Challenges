# Challenge #9, Squares

This solution makes use of `Counter` from the in-built `collections` library. The creation of the Counter object, `abs_counter` is an O(n) operation as can be seen from the [source code](https://hg.python.org/cpython/file/2.7/Lib/collections.py#l528).

1. To start off, we create an empty `output_list` which we will append our output.
2. Next, we create a Counter object `abs_counter` from the input list with the absolute values of each element within. 
3. The lowest and highest absolute values, `max_abs` and `min_abs` are found.
4. This allows us to iterate through all absolute values in ascending order, eliminating the need for any form of sorting after we square the elements. 
5. Put into practice: we iterate through from `min_abs` to `max_abs+1`, appending the squares accordingly (taking into account elements that occur more than once as well) into the output, `output_list`.

The unit test covers,

1. Positive integers
2. Negative integers
3. Zeroes
4. Repeat elements

```
......
----------------------------------------------------------------------
Ran 6 tests in 8.258s

OK
test_all completed 100000 reps with 1.8796267224919547s
test_negatives completed 100000 reps with 1.0380016055644727s
test_positives completed 100000 reps with 1.0510455415440965s
test_repeats completed 100000 reps with 2.041641256050432s
test_zeroes_negatives completed 100000 reps with 1.102484358268124s
test_zeroes_positives completed 100000 reps with 1.1347802273483003s
```
