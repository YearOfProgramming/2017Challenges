# Valid Closers
###### Language Version (Python 3.6.0)


For this challenge we implement a list as a stack. As we iterate through the
string input we add every opener found into the stack sequentially.

As the iteration continues onto the closers, check the if closer matches the last
element in our stack. If match is successful, pop the element off the stack and continue.
If any pair fails to match then the string input contains an invalid closer and
the function returns False.

After iteration is complete if our stack is empty then every opener had a valid
closer and the function returns True.


Run ```test.py``` to test code against the unit test.
```
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```
