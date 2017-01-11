# ValidClosers
###### Java 8

### 1. Approach to Solving the problem

Struggled for a while and looked at zmiller91's approach and derived something very similar
Once again his logic helped me learn much on this one!

### 2. How to compile and run this code


```
javac ValidClosers.java
java ValidClosers
```

### 3. How this program works

Track openers "(" "{" or "[" in one list, and closers in another.	
This problem pretty much requires a stack, which is last in first out. 
Put all the openers on the stack, which is the same but reverse order that closers
should be in the rest of the string.

eg. if we actually used two stacks, they would look like this:
```
openers = (, (, (
closers = ), ), )
```

So we continue iterating through the closers from "first to last", and compare "last to first" in the openers stack.
If we have a match, it's safe to pop it off the stack and check the next pair. If the stack's empty we know they all matched.
 