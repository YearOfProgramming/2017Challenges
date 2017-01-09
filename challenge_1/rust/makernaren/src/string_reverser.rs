/*Not an efficient solution, but I learnt arrays, vectors in rust and can't 
define run time array in rust :( */
pub fn reverse(input: &str) -> String {
	let n = input.len();
	// Define a vector of char type with length of the input string
	let mut char_vec = vec!['a'; n];
	// Replace the chars to tail of the vector
	for (i, c) in input.chars().enumerate() {
		char_vec[n-1-i] = c
		// char_array.push(c)
	}
	// Iterate, copy and collect it as a string
	let result: String = char_vec.iter().cloned().collect();
	return result
	// oneliner : return input.chars().rev().collect::<String>();
	
}


#[cfg(test)]
mod tests {
	use std::collections::HashMap;
	use super::*;
	#[test]
	fn test_string_reverse() {
		let mut test_cases = HashMap::new();
		test_cases.insert("hello", "olleh");
		test_cases.insert("rust", "tsur");
		test_cases.insert("I am a rustecean", "naecetsur a ma I");
		for (input, expected) in test_cases.iter() {
			assert_eq!(expected.to_owned(), reverse(input));	
		}
	}
}
