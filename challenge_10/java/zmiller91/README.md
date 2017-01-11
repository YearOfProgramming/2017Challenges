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

* `openers` get pushed to the stack
* `openers` will be poped from the stack if the `closers` meet the following conditions:
   * `stack` is not empty
   * The first element on the stack is in `openers`
   * The `closers` must close the `openers` popped from the `stack`
* `stack` must be empty after the string has been processed