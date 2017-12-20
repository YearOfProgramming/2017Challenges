extern crate challenge_5;
use challenge_5::find_odd_letter;
use std::fs;
use std::io;
use std::fs::File;
use std::path::Path;

#[test]
fn readme_test(){
    let s = "abcd";
    let t = "abcde";

    assert_eq!(find_odd_letter(s, t).unwrap(), 'e');
}

#[test]
fn much_longer_test() {
    let s = "abcdefghijklmnopqrstuvwxy";
    let t = "yxwvutsrqpoznmlkjihgfedcba";

    assert_eq!(find_odd_letter(s, t).unwrap(), 'z');
}
