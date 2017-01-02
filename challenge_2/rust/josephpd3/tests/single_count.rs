extern crate josephpd3;

use josephpd3::*;

#[test]
fn lonely_hearts_club() {
    let v = vec!['1', '1', '2', 'a', 'b', 'b', 'b', 'c', 'c'];
    assert_eq!(get_lonely_items(&v), vec!['2', 'a']);
}

#[test]
fn for_never_alone() {
    let v = vec!['1', '1', '2', '2', 'a', 'a', 'b', 'b', 'b', 'c', 'c'];
    assert_eq!(get_lonely_items(&v), vec![]);
}