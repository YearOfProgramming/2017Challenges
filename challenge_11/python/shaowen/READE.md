###Challenge 11

Language Version: Python 2.7.12


### Solution

As I don't have much exprerience with bst before, so I first check the algorithms from the following link, before I implement it in python. I think the illustration is very clear, one could easily get the idea just by going through the graphs. So I would recommend to anyone who is not familiar with the algorithm behind.

(but java guys should be careful, a java version of implementation is down the page.)

http://www.algolist.net/Data_structures/Binary_search_tree/Removal

### How to run
As requested, the program is designed to be interactive, so here it is.

$ python bst.py

Please type in a list of node integer, seperated by space.

(now you could type in a list of number just like following to set up the bst)

5 2 1 3 12 9 21 19 36

Original bst list: 

[5, 2, 1, 3, 12, 9, 21, 19, 36]


Please type in key(s) you want to delete:

(now you could type in one int, or a list of int like following, if the key is not in bst, you will also be notified.)

5 7 2 19

key 7 not found.

New bst list:

[9, 3, 1, 12, 21, 36]



###Testing

$ python unit_test.py
