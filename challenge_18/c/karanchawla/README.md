```
Karan Chawla
Challenge 18
```

The aim of the challenge was to calculate the number of paths from one extreme end to another. The problem was solved recursively by counting the possible number of paths from the two options available at each step.
Since diagnol moves are not allowed - at each step there's only two options - go right or go up. For each decision there are a set of paths which are counted recursively. 

Like so 
```
numberOfPaths(n-1,m) + numberOfPaths(n,m-1)  
```