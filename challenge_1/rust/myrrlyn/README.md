# String Reversal

This one is actually a *really tricky question*.

You'd think that just looping across the bytes in reverse order would work, but
unfortunately text is way harder than that.

So while standard library usage may be cheating; it's what we should do in real
cases where multi-byte characters or grapheme clusters (yeah, Unicode is *wild*)
may happen.

## Usage

If you don't have Rust, install it through your package manager or [Rustup].

```
$ cd challenge_1/rust/myrrlyn
$ cargo run
```

[Rustup]: https://rustup.rs/
