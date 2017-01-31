# ReversingALinkedList
###### Java 8

### 1. Approach to Solving the problem

Build a normal linked list, then write a new function to reverse it.

### 2. How to compile and run this code

```
javac ReversingALinkedList.java
java ReversingALinkedList
```

### 3. How this program works

First the list is built by the word split by ' '
Then that list is passed into the reversing function, which happens in 3 steps

1. Capture the next node in the list
2. Switch current node with previous node
3. Increment previous node and current node by one position

These are the 3 steps needed to reverse a list. At the end, the previous node will be the
new head
