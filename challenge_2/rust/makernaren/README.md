## Single Number
#### To run the code : 
* Open this directory in terminal and run `cargo run` to compile and run the code.
* To test the code just run, `cargo test` in same directory.
```
$ cargo run
    Finished debug [unoptimized + debuginfo] target(s) in 0.62 secs
     Running `target/debug/makernaren`
Given array is [1, 1, 2, 2, 3, 3, 5] 
Single occurance : 5

$ cargo test
    Finished debug [unoptimized + debuginfo] target(s) in 0.70 secs
     Running target/debug/makernaren-bf4fafb462d1be5f
running 1 test
test single_number::tests::test_int ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured