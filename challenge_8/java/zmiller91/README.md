# Random Pointer Linked List

This algorithm creates a deep copy of a linked list with random pointers in O(N)
time and space.  It allows duplicated data to exist as well. Here's how it works:


A HashMap `ogIndexes` stores a node's index, given a reference to itself: 

```
{
    {7} => 0,
    {5} => 1,
    {3} => 2
}
```

A HashMap `cpObjects` stores a copied node, given it's index in the list

```
{
    0 => {7'},
    1 => {5'},
    2 => {3'}
}
```

Given this mapping, we can iterate through the original and copied linked lists.
During each iteration, we can set the copied node's random pointer to: 

```
cpNode.random = cpObjects.get(ogIndexes.get(ogNode.random));
```

Assume `cpNode = {7}`, `ogNode = {4}` `ogNode.random = {3}`. We know the original 
`{3}` is at index `2` therefore the copied `{3}` is at index `2`. We can get a
reference to the copied `{3}` via `cpObjects.get(2)`. Once we have the copied `{3}`
we can set `cpNode.random` and move on.