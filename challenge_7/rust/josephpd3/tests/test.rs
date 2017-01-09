extern crate josephpd3;

use josephpd3::get_missing_num;

pub fn generate_vec_to_num_without(max: u32, without: u32) -> Vec<u32> {
    (0..max)
        .filter(|&x| x != without)
        .collect::<Vec<u32>>()
}

#[test]
fn ordered() {
    let missing = 5u32;
    let n = 15u32;
    assert_eq!(
        get_missing_num(
            generate_vec_to_num_without(n, missing)
        ),
        missing
    );
}

#[test]
fn unordered() {
    assert_eq!(get_missing_num(vec![7, 5, 1, 0, 4, 3, 2, 8]), 6);
}
