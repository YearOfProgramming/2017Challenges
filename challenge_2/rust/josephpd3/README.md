# Lonely Hearts Club
--------

This module contains a function, `get_lonely_items`, which takes a slice of a character vector (characters being either digits or alphabetical characters) and returns a vector of those among the characters who are the "last of their kind"--in lexicographical order.

The function, in absolute worst case, runs in `2n` time, but in complexity can be considered `O(n)`.

```rust
let v = vec!['1', '1', '2', 'a', 'b', 'b', 'b', 'c', 'c'];
assert_eq!(get_lonely_items(&v), vec!['2', 'a']);
```

The test can be run using `cargo test` from within the package.
