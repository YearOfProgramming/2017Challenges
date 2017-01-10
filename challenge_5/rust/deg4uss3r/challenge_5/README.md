# Challenge_5
Looks for the odd letter in two strings

# How to run
```
extern crate challenge_5
use challenge_5::find_odd_letter;

find_odd_letter(shorter_str, added_letter_str); //return char
```

# How to execute the tests
Simply run `cargo test` in the repository otherwise create a function like so:

```
extern crate challenge_5
use challenge_5::find_odd_letter;

#[test]
fn test_odd_letter () {
    let s = "abc";
    let t = "abce";
    assert_eq!(find_odd_letter(s,t), 'e');
}
```
