# Challenge 2: Select Unique

This challenge reads a stream of incoming elements and emits those that only
occur once.

My solution works by maintaining a dictionary of characters seen and their
count. The dictionary has O(1) access time per element, and so takes O(n) time
to fully populate. Once the dictionary is populated, it is drained (also O(n)
time), filtered for uniqueness, and the surviving elements are printed.

I considered using other implementation methods, such as keeping two lists: one
of uniques and one of duplicates. When a character arrives, we search the list
of duplicates for it. If it's there, skip. If it's not, search the list of
uniques. If it's there, remove it, and insert it into duplicates. If not, insert
it. At the end, the list of uniques is ready to be printed.

## Usage

This cannot be run on the stable or beta channels at present, due to the use of
feature flags.

```
$ rustup override set nightly
$ cargo test
Unique element: 5
$ echo "1234321 abcdcba" | cargo run
Unique element: 4
Unique element: d
$ cargo run
# Start typing in some characters
0987890 qwertrewq
# Hit ctrl-d to close standard input
^D
Unique element: 7
Unique element: t
```
