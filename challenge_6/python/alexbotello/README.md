# Ranges
###### Language Version (Python 3.6.0)

First, we must set a couple of variable flags to keep track of the array
sequence and initialize our ```ranges``` list. We'll choose ```begin``` and ```end```
as sufficient flag names. Next, we iterate through the input array and set the
value of our flags to equal the first element. For every iteration after, if the
next element is in sequence to the previous, we update our `end` flag to equal
the current element. Once, we iterate to an element that breaks the sequence we
append our flag values to our ```ranges``` list and reset flags to the current
element. Finally, after the for loop is complete, make a final comparison of
```begin``` and ```end``` to check if a final range sequence exists.

### Compile
Run ```tests.py``` to check against unit test
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

Run ```ranges.py``` to test your own implementation
First input should be the size of your array. Subsequent inputs will be the values
of the array.


Unit Test written by: slandau3
