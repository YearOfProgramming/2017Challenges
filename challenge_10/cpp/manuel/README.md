# Valid Closers
###### C++11 @manuel

### 1. Approch to Solving the problem

To solve this challenge I used a map to count the closers.

If we had a left bracket we incremented the map to it by one.

If we had a right bracket, we decremented the map to the corresponding
left bracket by one.

If at any point, the counter fell below 0, then there was a right
bracket without a corresponding left bracket and the test was False;

At the end of all the keys returna a value of 0, then all the brackets
were closed.

### 2. How to compile and run this code

```
make
make test 
make clean
```

### 3. How this program works

Single line of input -> Single line of output
