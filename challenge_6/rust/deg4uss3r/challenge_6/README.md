# Challenge_6
Making strings of numbers print out like "1->5" if consecutive 

# How to run
Check out ./example/main.rs to see how it works :)

```
extern crate challenge_6
use challenge_6::string_numbers

string_numbers(vec_of_u32);
```

The function `string_numbers` returns a Vec<String> of each run

# How to test
Simply run `cargo test` to run the built in tests

I have constructed the tests like so:

```
let test_vec: Vec<u32> = vec!(1,2,3,4,6);
assert_eq!(string_numbers(test_vec),vec!("1->4"));
```
