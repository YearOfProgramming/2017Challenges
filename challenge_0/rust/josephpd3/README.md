# Hello, World!
--------

Instead of just compiling a new binary Rust package, I thought fiddling with macros and testing them would be a fun, easy start.

The macro herein can be used in two ways.

```rust
hello!() // returns the string: "Hello, World!"
hello!("Joe") // returns the string: "Hello, Joe!"
```

You can run `cargo test` from within the package to run the tests.
