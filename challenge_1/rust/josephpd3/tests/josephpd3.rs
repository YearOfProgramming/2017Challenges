extern crate josephpd3;

use josephpd3::*;

#[test]
fn reverse_string() {
    let s: String = "hello".to_owned();
    assert_eq!("olleh".to_owned(), reverse(s.as_str()));
}
