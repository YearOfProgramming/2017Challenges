mod single_number;
fn main() {
    // let input = vec!['a', 'a', 'b', 'b', 'c', 'c', 'd'];
   	let input = vec![1, 1, 2, 2, 3, 3, 5];
    println!("Given array is {:?} \n Single occurance : {}",input.clone(), single_number::find_single(input));
    
}