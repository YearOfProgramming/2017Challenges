# Valid Closers

## How to run

```
javac ValidClosers.java 
java ValidClosers
```

## Discussion

* Runtime: O(n)
* Space: O(n)

The solution is a stack implementation, the stack must follow these rules:

1. `openers` get pushed to the stack
2. `openers` will be poped from the stack if the closers meet the following conditions:
   a. `stack` is not empty
   b. The first element on the stack is an `openers`
   c. The `closers` must match the `opners` popped from the `stack`
3. `stack` must be empty after the string has been processed