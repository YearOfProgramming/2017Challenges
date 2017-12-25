```
Karan Chawla
Challenge 11
```

This one was a bit tricky to solve but once you think of all the cases, shouldn't be very difficult. 
The problem can be broken down into 3 cases:
- 1. If the node to be deleted is a leaf node - in which case you just delete the node.
- 2. If the node to be deleted has one child - in which case you copy the child to the node and delete the child. 
- 3. If the node to be deleted has two children - find the successor in right subtree - copy it to the node and delete the successor node.

This is the high level picture - but the implementation may be riddled with more segmentation faults than you'd like, stick with it. You'll get it sooner or later. 

 