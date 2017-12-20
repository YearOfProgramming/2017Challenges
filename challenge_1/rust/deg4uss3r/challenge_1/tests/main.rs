extern crate challenge_1;
use challenge_1::string_reverse;

#[test]
fn hello_test() {
    assert_eq!(string_reverse("hello".to_string()), "olleh".to_string());
}
