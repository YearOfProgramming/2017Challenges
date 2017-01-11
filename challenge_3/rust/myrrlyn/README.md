# Challenge 3

This solution uses the exact same overally structure as my Challenge 2 solution.
A function consumes a vector of some type (I splurged and set it to be generic
over any type that implements `Display`, `Eq`, and `Hash`) and emits a result.

In this case, the function returns something or nothing. Coincidentally, these
are the exact discriminants that compose `Option<T>`, so the function returns
an `Option<(T, i32, usize>)` where `T` is the type being scanned. The tuple is
composed of the member of `T` with majority occurrence in the set, the `i32`
count of occurrences, and the `usize` count of total elements in the set.

The library function is consumed by the main executable, which matches on the
result. For `Some(result)`, it prints the element, count, and total; for `None`,
it sadly informs us that no majority element occurs.

This also requires nightly Rust.

## Usage

1. [Install Rustup][https://rustup.rs] if you have not yet done so.
1. Do `rustup toolchain install nightly` if you have not yet done so.
1. Do `cd challenge_3/rust/myrrlyn; rustup override set nightly`.
1. Do `cargo test` to see tests pass.
1. Do `echo "1 2 2 3 3 3 3" | cargo run` to see it work on your input.
1. Do `echo "1 2 3 3" | cargo run` to see it not work on your input.
1. Do `cargo run` to have it await your input. You'll need to hit enter, then
    ctrl-D, to close standard input. I collect ALL input, rather than looping
    over lines. I may want to change that in the future.
