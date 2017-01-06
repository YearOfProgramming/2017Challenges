(Python 3.5)
Given two input strings s and t, where t is a scrambled version of s with a new
character inserted somewhere at random in the string, finds the new character.
Collects frequencies of characters in s and t and matches them to find anomaly.

FindTheDifference.py contains two versions of the same function,
the older version (findTheDifference_old) uses two dicts to count frequency of characters manually;
the newer version (findTheDifference) uses the Counter function from collections module. 

### To run test, either run:
	python FindTheDifference.py

Time comparisons are presented below.

Output:
Test1 - Counter: 0.00027 seconds
e
Test1 - dicts: 0.00077 seconds
P
Test2 - Counter: 0.00082 seconds
P
Test2 - dicts: 0.00097 seconds
None
Test3 - Counter: 0.00071 seconds
None
Test3 - dicts: 0.00085 seconds


### Or use test.py (copied from mjuiuc's folder for convenience, edited for python 3):
	python test.py

Note: This calls only the version of the function using Counter.

Output:
Runtime of Case1: 0.0 seconds
.Runtime of Case2: 0.0 seconds
.Runtime of Case3: 0.0 seconds
.Runtime of Case4: 0.0 seconds
.Runtime of Case5: 0.0005004405975341797 seconds
.
----------------------------------------------------------------------
Ran 5 tests in 0.010s

OK
