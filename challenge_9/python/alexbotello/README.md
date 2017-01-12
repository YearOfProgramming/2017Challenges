# Squares
###### Language Version (Python 3.6.0)


First, we need to find and separate the positive and negative values from the original array.
Next we reverse the array holding our negative values.
This is done to ensure order will be preserved once array is squared.
Without the reversal our array becomes unsorted [-5, -4] -> [25, 16]
Iterate to compare negative and positive arrays and append the smallest value.
Continues the iteration until our resultant array matches the length of our original array.

### Compile

```
python test.py
```

```
python square.py
```

### How To Use

Run test.py to check different test cases

Run python square.py to test your own implementation
First input line is the number of elements in your array
Subsequent input lines are the array values

Unit Test Written By: slandau3
