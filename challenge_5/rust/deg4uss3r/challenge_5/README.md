# Challenge_5
Looks for the odd letter in two strings

# How to run
```
extern crate challenge_5
use challenge_5::find_odd_letter;

find_odd_letter(shorter_str, added_letter_str); //returns an option<char> or option<None>
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

I have also utilized the python unit tests located in ./target/debug/examples/main
This will grab the files in testfiles and check if there is a difference between the strings seperated by a new line.
