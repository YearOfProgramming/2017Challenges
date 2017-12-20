extern crate challenge_6;
use challenge_6::string_numbers;

#[test]
fn test_one() {
    let tester: Vec<u32> = vec!(1,2,3,4,5,8,9,10);
    assert_eq!(string_numbers(tester), vec!("1->5","8->10"));
}

#[test]
fn test_two() {
    let new_test: Vec<u32> = vec!(1,2,3,4,9,10,15);
    assert_eq!(string_numbers(new_test), vec!("1->4", "9->10"));
}

#[test]
fn test_three() {
    let test_three: Vec<u32> = vec!(1,2,3,4,8,9,10,12,13,14);
    assert_eq!(string_numbers(test_three), vec!("1->4","8->10","12->14"));
}
