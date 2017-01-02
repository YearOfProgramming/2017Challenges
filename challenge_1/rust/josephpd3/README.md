# Reverse a String!
--------

Moved tests into their own directory for this one.

This is a single module with the function `reverse`, which takes a string reference/slice, `&str`, and returns a `std::string::String`.

```rust
let s: String = "hello".to_owned();
assert_eq!("olleh".to_owned(), reverse(s.as_str()));
```

To run tests, run `cargo test` in package.
