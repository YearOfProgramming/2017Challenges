extern crate josephpd3;

use josephpd3::get_sorted_squares;

#[test]
fn contiguous_through_zero() {
    let v = vec![-4, -3, -2, -1, 0, 1, 2, 3];
    assert_eq!(get_sorted_squares(v), vec![0, 1, 1, 4, 4, 9, 9, 16]);
}

#[test]
fn noncontiguous_through_zero() {
    let v = vec![-7, -4, -3, -2, -1, 0, 1, 2, 3, 5, 8, 9];
    assert_eq!(
        get_sorted_squares(v),
        vec![0, 1, 1, 4, 4, 9, 9, 16, 25, 49, 64, 81]
    );
}

#[test]
fn all_above_zero() {
    let v = vec![1, 2, 3, 4, 5];
    assert_eq!(get_sorted_squares(v), vec![1, 4, 9, 16, 25]);
}

#[test]
fn all_below_zero() {
    let v = vec![-5, -4, -3, -2, -1];
    assert_eq!(get_sorted_squares(v), vec![1, 4, 9, 16, 25]);
}
