mod multi_occurance;
fn main() {
    // let input = vec!['a', 'a', 'b', 'b', 'c', 'c', 'd'];
   	let input = vec![1, 1, 2, 2, 3, 3, 3, 3, 5];
    println!("Given array is {:?} \n Majority occurace : {}",input.clone(), multi_occurance::find_majority(input));
    
}