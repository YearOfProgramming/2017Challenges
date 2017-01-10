# Challenge_3
Solved using a loop over the vector and a HashMap to count the number of times we see each number. 

If the number is larger than the size of the vector/2 as per the istructions return the number quickly.

# How to use
```
extern crate challenge_3;
use challenge_3::majority_finder;

majority_finder(vector: Vec<u64>); //returns u64 
```

## How to test
Simply run `cargo test` in the directory to see the test file located in ./tests/main.rs
