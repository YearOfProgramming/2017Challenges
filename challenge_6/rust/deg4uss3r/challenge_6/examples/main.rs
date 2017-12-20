extern crate challenge_6;
use challenge_6::string_numbers;
use std::vec::Vec;

fn main() {
    let tester: Vec<u32> = vec!(1,2,3,4,5,8,9,10);
    println!("{:?}", string_numbers(tester));

    let new_test: Vec<u32> = vec!(1,2,3,4,9,10,15);
    println!("{:?}", string_numbers(new_test));

    let test_three: Vec<u32> = vec!(1,2,3,4,8,9,10,12,13,14);
    println!("{:?}", string_numbers(test_three));
}
