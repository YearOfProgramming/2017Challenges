# Challenge 6, Ranges

1. A copy of the `input_list`, called `output_elements`, is created. This is to avoid modifications to the original list while we iterate through it. The `output_elements` will hold integers that belong to a range, i.e. those in [0, 1, 2, 3, 4], but not [0, 2, 4].

2. A list named `output_list` is created. This will be the list that the function will return, with elements formatted in the required style of `'x->y'`.

3. We iterate through the list with two conditionals. The first checks if for an integer `x`, if `x-1` or `x+1` exists in the `input_list`. If `x-1` and `x+1` does not exist, this means that `x` is a 'loner' that does not belong in a range, and is thus removed from consideration as our output (`output_elements.remove(integer)`.

4. The second conditional within this first iteration checks if for an integer `x`, if both `x-1` and `x+1` exists. If true, this means that the integer `x` is contained within the range (i.e. not belonging to either ends of the range). We remove this from our `output_elements` so we can simplify `output_elements` to include only the two extremes for each range (i.e. for `'x->y'`, only contain `[x, y]`).

5. We iterate once more, this time through the `output_elements` and using `enumerate`. This final iteration serves the purpose of formatting `output_elements` into the expected presentation of `output_list`.

## Unit Test

`test.py` is the unit test I created for this challenge. It includes tests for

1. 'Empty' `input_list` of empty array
2. 'Small' `input_list` of one range
3. 'Single' `input_list` of a single integer
4. 'Large' `input_list` of two ranges
5. 'Larger' `input_list` of five ranges
6. 'Largest' `input_list` of ten ranges
7. 'Negatives' `input_list` of three ranges, with two including negative integers

## Learning Points

1. `list_1 = list_2` is an assignment; `list_1 = list(list_2)` is a copy
2. Naming your unit test `unittest.py` is one bad idea...
