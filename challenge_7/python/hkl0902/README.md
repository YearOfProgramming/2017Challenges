# Find the Missing Number

The solution to this problem will leverage the following:

1 + 2 + 3 + ... + N = N(N+1)/2  

Therefore, if `x` is missing and I'm given the list LST, `x = N(N+1)/2 - sum(LST)`

I merely need the LST and a way to sum it up (which I can do via a simple for loop) or the inbuilt `sum` function. 
