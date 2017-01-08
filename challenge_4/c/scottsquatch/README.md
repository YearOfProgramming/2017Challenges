# Reverse a binary tree
Reverse a binary tree.

## Building
``` bash
make
```

## Running
``` bash
./reverse_tree <Input File>
```
Input file will contain a series of space separated integers to insert into
tree. Example: ```1 2 3 4```. The reversed tree will be output to the screen
using Breadth-First Search. For example, if given a tree:
```
    6
   / \
  3   9
 / \  /\
2  4 7 10
```
the output to the screen will be ```6 3 9 2 4 7 10```.

## Cleanup
``` bash
make clean
```

## Tests
``` bash
make test
./bin/binary_tree_reverse_tests
```
